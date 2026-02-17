# zwave-specs-mcp -- Z-Wave Specification MCP Server

An MCP (Model Context Protocol) server that parses, indexes, and serves
[Z-Wave specification](https://github.com/zwave-js/specs) content through
MCP tools for LLM consumption. Query Command Classes, registries, device
types, test specifications, and more.

## Installation

Requires Python 3.13+.

```bash
cd mcp
uv sync
```

## Running

```bash
zwave-specs-mcp --specs-dir /path/to/specs
```

Or without installing:

```bash
uv run python -m mcp_zwave_specs --specs-dir /path/to/specs
```

If the `mcp/` directory lives inside the specs checkout (the default
layout of this repository), the specs directory is auto-detected and
`--specs-dir` can be omitted.

## Configuration

Three configuration methods are supported. Precedence order:

**CLI flags > TOML config file > Environment variables > Built-in defaults**

### CLI Flags

| Flag | Description |
|------|-------------|
| `--specs-dir PATH` | Path to zwave-js/specs checkout |
| `--cache-dir PATH` | Cache directory (default: `~/.cache/mcp/zwave-specs`) |
| `--config PATH` | Path to TOML configuration file |
| `--clear-cache` | Clear cache before starting |

### TOML Config File

Pass a TOML file with `--config path/to/zwave-specs-mcp.toml`. All keys are
optional; only specified values override the defaults.

```toml
# Base directories
specs_dir = "~/projects/specs"
cache_dir = "~/.cache/mcp/zwave-specs"

# Individual file path overrides (relative to specs_dir)
[paths]
app_layer_pdf = "Z-Wave Specification AWG V5.0.pdf"
header_file = "API_includes/ZW_classcmd.h"
cc_list_xlsx = "Z-Wave Command Classes Specifications/List of defined Z-Wave Command Classes.xlsx"
network_layer_pdf = "Z-Wave Stack Specifications/Z-Wave and Z-Wave Long Range Network Layer Specification.pdf"
host_api_pdf = "Z-Wave Stack Specifications/Z-Wave Host API Specification.pdf"

# Stack specification PDFs (key = tool lookup key, value = filename)
[supplementary_pdfs]
network_layer = "Z-Wave and Z-Wave Long Range Network Layer Specification.pdf"
host_api = "Z-Wave Host API Specification.pdf"
long_range_phy_mac = "Z-Wave Long Range PHY and MAC Layer Specification.pdf"

# Test specification PDFs
[test_pdfs]
test_phy = "Z-Wave PHY Layer Test Specification.pdf"
test_mac = "Z-Wave MAC Layer Test Specification.pdf"
test_network = "Z-Wave Network Layer Test Specification.pdf"
test_lr_phy = "Z-Wave Long Range PHY Layer Test Specification.pdf"
test_lr_mac = "Z-Wave Long Range MAC Layer Test Specification.pdf"
test_lr_network = "Z-Wave Long Range Network Layer Test Specification.pdf"

# Legacy specification PDFs
[legacy_pdfs]
legacy_500_app_guide = "500 Series Application Programmers Guide.pdf"
legacy_500_serial_api = "500 Series Serial API Specs.pdf"
legacy_device_class = "Z-Wave Device Class Specification.pdf"
legacy_zwaveplus_v1_device_type = "ZWA_Z-Wave Plus Device Type Specification 33.0.0.pdf"
legacy_app_layer_v1 = "Z-Wave Specification AWG V1.0.pdf"
legacy_app_layer_v2 = "Z-Wave Specification AWG V2.0.pdf"
legacy_app_layer_v3 = "Z-Wave Specification AWG V3.0.pdf"

# Standalone PDFs (not inside a subdirectory)
[standalone_pdfs]
security_s0 = "SDS10865-Z-Wave-Application-Security-Layer-S0.pdf"
```

### Environment Variables

Base directories:

- `ZWAVE_SPECS_MCP_SPECS_DIR` -- path to the specs checkout
- `ZWAVE_SPECS_MCP_CACHE_DIR` -- cache directory
Individual path overrides use the `ZWAVE_SPECS_MCP_` prefix with the key name in
uppercase:

```bash
export ZWAVE_SPECS_MCP_APP_LAYER_PDF="Z-Wave Specification AWG V5.0.pdf"
export ZWAVE_SPECS_MCP_HEADER_FILE="API_includes/ZW_classcmd.h"
```

Category dict entries use a double underscore to separate the group name
from the key:

```bash
export ZWAVE_SPECS_MCP_LEGACY_PDFS__LEGACY_AWG_V4="Z-Wave Specification AWG V4.0.pdf"
export ZWAVE_SPECS_MCP_TEST_PDFS__TEST_SECURITY="Z-Wave Security Test Specification.pdf"
```

## MCP Tools Reference

The server exposes 19 tools. Parameters marked with `| None` accept `null`
to use their default behavior.

### Command Class Tools

#### list_command_classes

List all Z-Wave Command Classes with IDs, versions, and status.

| Parameter | Type | Description |
|-----------|------|-------------|
| `category` | `str \| None` | Filter by category: `application`, `management`, `transport`, `network`, `control` |
| `include_deprecated` | `bool` | Include deprecated/obsoleted CCs (default: `false`) |

#### get_command_class

Get the full specification text for a Command Class.

| Parameter | Type | Description |
|-----------|------|-------------|
| `name` | `str \| None` | CC name, fuzzy-matched (e.g., `"Door Lock"`) |
| `cc_id` | `int \| None` | CC ID as integer (e.g., `98` for `0x62`) |
| `version` | `int \| None` | Specific version number |

#### search_command_classes

Search across all CC specifications.

| Parameter | Type | Description |
|-----------|------|-------------|
| `query` | `str` | Search terms (e.g., `"thermostat setpoint"`) |
| `max_results` | `int` | Maximum results to return (default: `5`) |

#### get_cc_commands

Get commands, opcodes, and frame struct definitions from the C header.

| Parameter | Type | Description |
|-----------|------|-------------|
| `name` | `str \| None` | CC name, fuzzy-matched |
| `cc_id` | `int \| None` | CC ID as integer |

### Registry Tools

#### lookup_notification

Look up Notification CC types and events.

| Parameter | Type | Description |
|-----------|------|-------------|
| `notification_type` | `str \| None` | Filter by type name (e.g., `"Smoke"`, `"Access Control"`) |
| `event` | `str \| None` | Search for event text |

#### lookup_sensor_type

Look up Multilevel Sensor types, scales, and units.

| Parameter | Type | Description |
|-----------|------|-------------|
| `sensor_type` | `str \| None` | Filter by sensor type name (e.g., `"Temperature"`) |

#### lookup_manufacturer

Look up manufacturer name or ID.

| Parameter | Type | Description |
|-----------|------|-------------|
| `name` | `str \| None` | Manufacturer name to search for |
| `manufacturer_id` | `str \| None` | Manufacturer ID hex string (e.g., `"0x0086"`) |

#### lookup_registry

Generic lookup for any Z-Wave registry.

| Parameter | Type | Description |
|-----------|------|-------------|
| `registry` | `str` | Registry key (e.g., `"icon_types"`, `"indicator_types"`, `"command_classes"`). Use `list_spec_documents()` to see all. |
| `search` | `str \| None` | Search text to filter rows |

#### get_lifeline_requirements

Mandatory Lifeline Association Group commands.

| Parameter | Type | Description |
|-----------|------|-------------|
| `command_class` | `str \| None` | CC name (e.g., `"Door Lock"`). Omit to list all. |

### Spec Document Tools

#### get_spec_section

Read a section from supplementary spec documents.

| Parameter | Type | Description |
|-----------|------|-------------|
| `pdf` | `str` | PDF key (e.g., `"network_layer"`, `"host_api"`) |
| `section` | `str \| None` | Section title or number |
| `search` | `str \| None` | Search text to find relevant section |

#### list_spec_documents

List all available spec documents, registries, and their contents. No
parameters.

#### search_application_notes

Search Application Notes (APL/INS documents).

| Parameter | Type | Description |
|-----------|------|-------------|
| `search` | `str \| None` | Search text. Omit to list all available notes. |

#### get_test_spec

Test specifications for certification compliance.

| Parameter | Type | Description |
|-----------|------|-------------|
| `pdf` | `str \| None` | Test spec key (e.g., `"test_phy"`, `"test_mac"`). Omit to list available. |
| `search` | `str \| None` | Search text within a specific test spec |

#### get_legacy_spec

Legacy Z-Wave specifications.

| Parameter | Type | Description |
|-----------|------|-------------|
| `pdf` | `str \| None` | Legacy spec key (e.g., `"legacy_500_app_guide"`). Omit to list available. |
| `section` | `str \| None` | Section title to retrieve |
| `search` | `str \| None` | Search text within the spec |

### Application Layer Chapter Tools

#### get_device_type

Device Type definition from application layer spec, Chapter 7. Includes
mandatory and recommended CC requirements.

| Parameter | Type | Description |
|-----------|------|-------------|
| `name` | `str \| None` | Device type name (e.g., `"Thermostat"`). Omit to list all. |

#### get_role_type

Role Type definition from application layer spec, Chapter 8 (CSC, SSC, PC, RPC, PEN, AOEN,
etc.).

| Parameter | Type | Description |
|-----------|------|-------------|
| `name` | `str \| None` | Role type name or abbreviation. Omit to list all. |

#### get_cc_interview_steps

CC interview/control requirements from application layer spec, Chapter 6.

| Parameter | Type | Description |
|-----------|------|-------------|
| `name` | `str \| None` | CC name (e.g., `"Door Lock"`). Omit to list all. |

### Device Class and Header Tools

#### get_device_class

Legacy Device Class lookup from `ZW_classcmd.h`.

| Parameter | Type | Description |
|-----------|------|-------------|
| `generic` | `str \| None` | Generic device class name (e.g., `"Switch Binary"`) |
| `specific` | `str \| None` | Specific device class name to search for |
| `generic_id` | `int \| None` | Generic device class ID (e.g., `16` for `0x10`) |

#### lookup_zwave_constants

Search Z-Wave C header constants (`#define` values).

| Parameter | Type | Description |
|-----------|------|-------------|
| `search` | `str` | Search text (matches define name or comment) |
| `header` | `str \| None` | Specific header file (e.g., `"ZW_SerialAPI.h"`). Omit to search all. |

## Adding or Overriding Spec Documents

To add a new PDF or override an existing one, use either the TOML config
file or environment variables.

**Via TOML** -- add an entry to the appropriate section. For example, to add
a new legacy spec:

```toml
[legacy_pdfs]
legacy_app_layer_v4 = "Z-Wave Specification AWG V4.0.pdf"
```

**Via environment variable** -- use the double-underscore syntax for
category entries:

```bash
export ZWAVE_SPECS_MCP_LEGACY_PDFS__LEGACY_AWG_V4="Z-Wave Specification AWG V4.0.pdf"
```

For individual path overrides (like a different AWG PDF location):

```bash
export ZWAVE_SPECS_MCP_APP_LAYER_PDF="custom/path/to/AWG.pdf"
```

New entries are merged with the built-in defaults. Setting a key that
already exists replaces the default value.

## License

AGPL-3.0 -- see [LICENSE](./LICENSE).
