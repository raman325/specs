"""Tests for CLI argument parsing and config layering."""

from pathlib import Path

from mcp_zwave_specs.cli import build_config, parse_args


def test_parse_args_config_flag():
    args = parse_args(["--config", "my.toml"])
    assert args.config == Path("my.toml")


def test_build_config_cli_overrides_toml(tmp_path):
    toml_file = tmp_path / "config.toml"
    toml_file.write_text('specs_dir = "/toml/specs"\n')
    args = parse_args(["--config", str(toml_file), "--specs-dir", "/cli/specs"])
    config = build_config(args)
    assert config.specs_dir == Path("/cli/specs")


def test_build_config_toml_overrides_env(tmp_path, monkeypatch):
    monkeypatch.setenv("ZWAVE_SPECS_MCP_SPECS_DIR", "/env/specs")
    toml_file = tmp_path / "config.toml"
    toml_file.write_text('specs_dir = "/toml/specs"\n')
    args = parse_args(["--config", str(toml_file)])
    config = build_config(args)
    assert config.specs_dir == Path("/toml/specs")
