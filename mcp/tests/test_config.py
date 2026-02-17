"""Tests for Config defaults and path resolution."""

from pathlib import Path

from mcp_zwave_specs.config import Config


def test_default_legacy_pdfs_include_awg_versions():
    """Legacy AWG V1-V3 should be in defaults."""
    config = Config(specs_dir=Path("/fake"))
    assert "legacy_app_layer_v1" in config.legacy_pdfs
    assert "legacy_app_layer_v2" in config.legacy_pdfs
    assert "legacy_app_layer_v3" in config.legacy_pdfs


def test_default_supplementary_pdfs():
    config = Config(specs_dir=Path("/fake"))
    assert "network_layer" in config.supplementary_pdfs
    assert "host_api" in config.supplementary_pdfs


def test_default_test_pdfs():
    config = Config(specs_dir=Path("/fake"))
    assert "test_phy" in config.test_pdfs
    assert "test_mac" in config.test_pdfs


def test_default_standalone_pdfs():
    config = Config(specs_dir=Path("/fake"))
    assert "security_s0" in config.standalone_pdfs


def test_app_layer_pdf_property_default():
    config = Config(specs_dir=Path("/specs"))
    assert config.app_layer_pdf == Path("/specs/Z-Wave Specification AWG V5.0.pdf")


def test_app_layer_pdf_override():
    config = Config(
        specs_dir=Path("/specs"),
        path_overrides={"app_layer_pdf": "Custom AWG.pdf"},
    )
    assert config.app_layer_pdf == Path("/specs/Custom AWG.pdf")


def test_from_env_specs_dir(monkeypatch):
    monkeypatch.setenv("ZWAVE_SPECS_MCP_SPECS_DIR", "/custom/specs")
    config = Config.from_env()
    assert config.specs_dir == Path("/custom/specs")


def test_from_env_path_override(monkeypatch):
    monkeypatch.setenv("ZWAVE_SPECS_MCP_APP_LAYER_PDF", "Custom AWG V6.0.pdf")
    config = Config.from_env()
    assert config.path_overrides["app_layer_pdf"] == "Custom AWG V6.0.pdf"


def test_from_env_category_dict_merge(monkeypatch):
    monkeypatch.setenv("ZWAVE_SPECS_MCP_LEGACY_PDFS__MY_CUSTOM", "custom.pdf")
    config = Config.from_env()
    assert config.legacy_pdfs["my_custom"] == "custom.pdf"
    # Defaults still present
    assert "legacy_500_app_guide" in config.legacy_pdfs


def test_from_env_category_dict_override(monkeypatch):
    monkeypatch.setenv(
        "ZWAVE_SPECS_MCP_LEGACY_PDFS__LEGACY_500_APP_GUIDE",
        "New 500 Guide.pdf",
    )
    config = Config.from_env()
    assert config.legacy_pdfs["legacy_500_app_guide"] == "New 500 Guide.pdf"


def test_merge_toml_paths(tmp_path):
    toml_file = tmp_path / "config.toml"
    toml_file.write_text('[paths]\napp_layer_pdf = "My Custom AWG.pdf"\n')
    config = Config(specs_dir=Path("/specs"))
    config.merge_toml(toml_file)
    assert config.path_overrides["app_layer_pdf"] == "My Custom AWG.pdf"


def test_merge_toml_legacy_pdfs(tmp_path):
    toml_file = tmp_path / "config.toml"
    toml_file.write_text(
        '[legacy_pdfs]\nlegacy_app_layer_v4 = "Z-Wave Specification AWG V4.0.pdf"\n'
    )
    config = Config(specs_dir=Path("/specs"))
    config.merge_toml(toml_file)
    assert config.legacy_pdfs["legacy_app_layer_v4"] == "Z-Wave Specification AWG V4.0.pdf"
    # Defaults still present
    assert "legacy_app_layer_v1" in config.legacy_pdfs


def test_merge_toml_specs_dir(tmp_path):
    toml_file = tmp_path / "config.toml"
    toml_file.write_text('specs_dir = "/toml/specs"\n')
    config = Config(specs_dir=Path("/original"))
    config.merge_toml(toml_file)
    assert config.specs_dir == Path("/toml/specs")


def test_merge_toml_cache_dir(tmp_path):
    toml_file = tmp_path / "config.toml"
    toml_file.write_text('cache_dir = "/toml/cache"\n')
    config = Config(specs_dir=Path("/specs"))
    config.merge_toml(toml_file)
    assert config.cache_dir == Path("/toml/cache")
