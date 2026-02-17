"""Configuration for zwave-specs-mcp server."""

from __future__ import annotations

import os
import tomllib
from dataclasses import dataclass, field
from pathlib import Path
from urllib.parse import quote

GITHUB_REPO = "zwave-js/specs"
GITHUB_BRANCH = "master"
GITHUB_BASE = f"https://github.com/{GITHUB_REPO}/blob/{GITHUB_BRANCH}"

DEFAULT_CACHE_DIR = Path.home() / ".cache" / "mcp" / "zwave-specs"

DEFAULT_SUPPLEMENTARY_PDFS: dict[str, str] = {
    "network_layer": "Z-Wave and Z-Wave Long Range Network Layer Specification.pdf",
    "host_api": "Z-Wave Host API Specification.pdf",
    "long_range_phy_mac": "Z-Wave Long Range PHY and MAC Layer Specification.pdf",
}

DEFAULT_TEST_PDFS: dict[str, str] = {
    "test_phy": "Z-Wave PHY Layer Test Specification.pdf",
    "test_mac": "Z-Wave MAC Layer Test Specification.pdf",
    "test_network": "Z-Wave Network Layer Test Specification.pdf",
    "test_lr_phy": "Z-Wave Long Range PHY Layer Test Specification.pdf",
    "test_lr_mac": "Z-Wave Long Range MAC Layer Test Specification.pdf",
    "test_lr_network": "Z-Wave Long Range Network Layer Test Specification.pdf",
}

DEFAULT_LEGACY_PDFS: dict[str, str] = {
    "legacy_500_app_guide": "500 Series Application Programmers Guide.pdf",
    "legacy_500_serial_api": "500 Series Serial API Specs.pdf",
    "legacy_device_class": "Z-Wave Device Class Specification.pdf",
    "legacy_zwaveplus_v1_device_type": "ZWA_Z-Wave Plus Device Type Specification 33.0.0.pdf",
    "legacy_app_layer_v1": "Z-Wave Specification AWG V1.0.pdf",
    "legacy_app_layer_v2": "Z-Wave Specification AWG V2.0.pdf",
    "legacy_app_layer_v3": "Z-Wave Specification AWG V3.0.pdf",
}

DEFAULT_STANDALONE_PDFS: dict[str, str] = {
    "security_s0": "SDS10865-Z-Wave-Application-Security-Layer-S0.pdf",
}

DEFAULT_PATHS: dict[str, str] = {
    "app_layer_pdf": "Z-Wave Specification AWG V5.0.pdf",
    "header_file": "API_includes/ZW_classcmd.h",
    "cc_list_xlsx": (
        "Z-Wave Command Classes Specifications/List of defined Z-Wave Command Classes.xlsx"
    ),
    "network_layer_pdf": (
        "Z-Wave Stack Specifications/Z-Wave and Z-Wave Long Range Network Layer Specification.pdf"
    ),
    "host_api_pdf": ("Z-Wave Stack Specifications/Z-Wave Host API Specification.pdf"),
}


@dataclass
class Config:
    specs_dir: Path
    cache_dir: Path = field(default_factory=lambda: DEFAULT_CACHE_DIR)
    github_base_url: str = GITHUB_BASE
    supplementary_pdfs: dict[str, str] = field(
        default_factory=lambda: dict(DEFAULT_SUPPLEMENTARY_PDFS)
    )
    test_pdfs: dict[str, str] = field(default_factory=lambda: dict(DEFAULT_TEST_PDFS))
    legacy_pdfs: dict[str, str] = field(default_factory=lambda: dict(DEFAULT_LEGACY_PDFS))
    standalone_pdfs: dict[str, str] = field(default_factory=lambda: dict(DEFAULT_STANDALONE_PDFS))
    path_overrides: dict[str, str] = field(default_factory=dict)
    app_layer_rst_dir: Path | None = None

    def __post_init__(self) -> None:
        """Resolve specs_dir and cache_dir to absolute paths."""
        self.specs_dir = Path(self.specs_dir).expanduser().resolve()
        self.cache_dir = Path(self.cache_dir).expanduser().resolve()
        if self.app_layer_rst_dir is not None:
            self.app_layer_rst_dir = Path(self.app_layer_rst_dir).expanduser().resolve()

    @property
    def specs_available(self) -> bool:
        """Return True if the specs directory exists on disk."""
        return self.specs_dir.is_dir()

    @property
    def app_layer_rst_available(self) -> bool:
        """Return True if an RST source directory is configured and exists."""
        return self.app_layer_rst_dir is not None and self.app_layer_rst_dir.is_dir()

    @property
    def app_layer_pdf(self) -> Path:
        """Absolute path to the application layer (AWG) PDF."""
        relative = self.path_overrides.get("app_layer_pdf", DEFAULT_PATHS["app_layer_pdf"])
        return self.specs_dir / relative

    @property
    def header_file(self) -> Path:
        """Absolute path to ZW_classcmd.h."""
        relative = self.path_overrides.get("header_file", DEFAULT_PATHS["header_file"])
        return self.specs_dir / relative

    @property
    def registries_dir(self) -> Path:
        """Absolute path to the Registries directory."""
        return self.specs_dir / "Registries"

    @property
    def cc_list_xlsx(self) -> Path:
        """Absolute path to the CC list Excel file."""
        relative = self.path_overrides.get("cc_list_xlsx", DEFAULT_PATHS["cc_list_xlsx"])
        return self.specs_dir / relative

    @property
    def network_layer_pdf(self) -> Path:
        """Absolute path to the network layer spec PDF."""
        relative = self.path_overrides.get("network_layer_pdf", DEFAULT_PATHS["network_layer_pdf"])
        return self.specs_dir / relative

    @property
    def host_api_pdf(self) -> Path:
        """Absolute path to the host API spec PDF."""
        relative = self.path_overrides.get("host_api_pdf", DEFAULT_PATHS["host_api_pdf"])
        return self.specs_dir / relative

    @property
    def smartstart_dir(self) -> Path:
        """Absolute path to the SmartStart Specifications directory."""
        return self.specs_dir / "SmartStart Specifications"

    @property
    def api_includes_dir(self) -> Path:
        """Absolute path to the API_includes header directory."""
        return self.specs_dir / "API_includes"

    @property
    def app_notes_dir(self) -> Path:
        """Absolute path to the Application Notes directory."""
        return self.specs_dir / "Application Notes"

    def github_url(self, relative_path: str) -> str:
        """Build a GitHub URL for a file in the specs repository."""
        encoded = quote(relative_path, safe="/")
        return f"{self.github_base_url}/{encoded}"

    @classmethod
    def from_env(cls) -> Config:
        """Build a Config from environment variables, merged with defaults."""
        # Default: specs repo root (two levels up from mcp_zwave_specs/ package directory)
        _pkg_dir = Path(__file__).resolve().parent  # mcp_zwave_specs/
        specs_dir = os.environ.get("ZWAVE_SPECS_MCP_SPECS_DIR", str(_pkg_dir.parent.parent))
        cache_dir = os.environ.get("ZWAVE_SPECS_MCP_CACHE_DIR", str(DEFAULT_CACHE_DIR))

        rst_dir = os.environ.get("ZWAVE_SPECS_MCP_APP_LAYER_RST_DIR")

        config = cls(
            specs_dir=Path(specs_dir),
            cache_dir=Path(cache_dir),
            app_layer_rst_dir=Path(rst_dir) if rst_dir else None,
        )

        # Known category group prefixes
        groups = {
            "SUPPLEMENTARY_PDFS": config.supplementary_pdfs,
            "TEST_PDFS": config.test_pdfs,
            "LEGACY_PDFS": config.legacy_pdfs,
            "STANDALONE_PDFS": config.standalone_pdfs,
        }
        # Known top-level keys (already handled above)
        top_level = {"SPECS_DIR", "CACHE_DIR", "APP_LAYER_RST_DIR"}

        prefix = "ZWAVE_SPECS_MCP_"
        for key, value in os.environ.items():
            if not key.startswith(prefix):
                continue
            suffix = key[len(prefix) :]
            if suffix in top_level:
                continue

            # Check for category dict: GROUP__KEY
            if "__" in suffix:
                group_name, dict_key = suffix.split("__", 1)
                if group_name in groups:
                    groups[group_name][dict_key.lower()] = value
                    continue

            # Otherwise treat as individual path override
            config.path_overrides[suffix.lower()] = value

        return config

    def merge_toml(self, path: Path) -> None:
        """Merge a TOML config file into this config. Values override existing."""
        with open(path, "rb") as f:
            data = tomllib.load(f)

        if "specs_dir" in data:
            self.specs_dir = Path(data["specs_dir"]).expanduser().resolve()
        if "cache_dir" in data:
            self.cache_dir = Path(data["cache_dir"]).expanduser().resolve()
        if "app_layer_rst_dir" in data:
            self.app_layer_rst_dir = Path(data["app_layer_rst_dir"]).expanduser().resolve()

        # Individual path overrides
        for key, value in data.get("paths", {}).items():
            self.path_overrides[key] = value

        # Category dict merges
        group_fields = {
            "supplementary_pdfs": self.supplementary_pdfs,
            "test_pdfs": self.test_pdfs,
            "legacy_pdfs": self.legacy_pdfs,
            "standalone_pdfs": self.standalone_pdfs,
        }
        for group_name, target_dict in group_fields.items():
            for key, value in data.get(group_name, {}).items():
                target_dict[key] = value
