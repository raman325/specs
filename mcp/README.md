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

#### RST Source Alternative

If you have the application layer spec as RST/Sphinx source (e.g. a
draft build directory), you can use it instead of the PDF. RST source
provides higher-fidelity text without PDF extraction artifacts.

```bash
uv run python -m mcp_zwave_specs --app-layer-rst-dir /path/to/rst-source/source
```

When configured, RST source is used for CC sections and chapter
sections (device types, role types, CC control). All other spec
documents still come from PDFs in `specs_dir`.

**Note:** The server uses a content-addressable disk cache — each
source file is cached under the MD5 hash of its content. Changing a
single PDF only re-extracts that file. Switching between spec versions
(e.g. v4 vs v5 AWG) is instant once both are warm. Because hashes are
content-based (not mtime-based), pre-built cache blobs can be committed
to the repository and shared across clones. Use `--write-gitignore` to
generate a `.cache/.gitignore` that tracks pre-built blobs while
ignoring user-generated ones.

### Development Mode

To open the MCP Inspector test UI for interactive tool testing:

```bash
uv run fastmcp dev mcp_zwave_specs/server.py
```

This launches a browser-based UI where you can call each tool, inspect
parameters, and see responses.

### Client Configuration

Example MCP server entries for AI coding tools. Each example
demonstrates a different configuration method -- see
[Configuration](#configuration) for details.

#### Claude Code (defaults)

In `.mcp.json` (project) or `~/.claude.json` (global). Uses
[built-in defaults](#defaults) -- no extra flags needed when the `mcp/`
directory is inside the specs checkout.

```jsonc
{
  "mcpServers": {
    "zwave-specs": {
      // Specs directory is auto-detected (two levels up from the package).
      // Cache goes to <specs-dir>/.cache.
      // See "Defaults" under Configuration to see all built-in values.
      "command": "uv",
      "args": ["run", "--directory", "/path/to/specs/mcp", "zwave-specs-mcp"]
    }
  }
}
```

#### GitHub Copilot (environment variables)

In `.vscode/mcp.json`. Overrides settings via `ZWAVE_SPECS_MCP_*`
environment variables -- see
[Environment Variables](#environment-variables) for the full list.

```jsonc
{
  "servers": {
    "zwave-specs": {
      "command": "uv",
      "args": ["run", "--directory", "/path/to/specs/mcp", "zwave-specs-mcp"],
      "env": {
        // Override the specs checkout location
        "ZWAVE_SPECS_MCP_SPECS_DIR": "/custom/path/to/specs",
        // Override the cache directory
        "ZWAVE_SPECS_MCP_CACHE_DIR": "/tmp"
        // Use RST source instead of PDF for the application layer spec:
        // "ZWAVE_SPECS_MCP_APP_LAYER_RST_DIR": "/path/to/rst-source/source"
      }
    }
  }
}
```

#### Gemini CLI (CLI flags)

In `~/.gemini/settings.json`. Passes flags directly as CLI arguments --
see [CLI Flags](#cli-flags) for all options.

```jsonc
{
  "mcpServers": {
    "zwave-specs": {
      "command": "uv",
      "args": [
        "run", "--directory", "/path/to/specs/mcp",
        "zwave-specs-mcp",
        // Point to a specs checkout in a non-standard location
        "--specs-dir", "/custom/path/to/specs",
        // Rebuild the cache on startup
        "--clear-cache"
      ]
    }
  }
}
```

#### OpenAI Codex CLI (TOML config file)

In `~/.codex/config.json`. Points to a TOML file for detailed overrides
-- see [TOML Config File](#toml-config-file) for the full format.

```jsonc
{
  "mcpServers": {
    "zwave-specs": {
      "command": "uv",
      "args": [
        "run", "--directory", "/path/to/specs/mcp",
        "zwave-specs-mcp",
        // All settings in one file -- individual paths, PDF groups, etc.
        "--config", "/path/to/zwave-specs-mcp.toml"
      ]
    }
  }
}
```

## Configuration

Three configuration methods are supported. Precedence order:

**CLI flags > TOML config file > Environment variables > Built-in defaults**

### Defaults

With no flags, environment variables, or config file the server uses
these built-in defaults:

| Setting | Default |
|---------|---------|
| `specs_dir` | Auto-detected (two levels up from the package directory) |
| `cache_dir` | `<specs_dir>/.cache` (`.cache` is appended automatically if missing) |
| `app_layer_rst_dir` | Not set (uses PDF by default) |
| `app_layer_pdf` | `Z-Wave Specification AWG V5.0.pdf` |
| `header_file` | `API_includes/ZW_classcmd.h` |
| `cc_list_xlsx` | `Z-Wave Command Classes Specifications/List of defined Z-Wave Command Classes.xlsx` |
| `network_layer_pdf` | `Z-Wave Stack Specifications/Z-Wave and Z-Wave Long Range Network Layer Specification.pdf` |
| `host_api_pdf` | `Z-Wave Stack Specifications/Z-Wave Host API Specification.pdf` |

PDF groups (`supplementary_pdfs`, `test_pdfs`, `legacy_pdfs`,
`standalone_pdfs`) also ship with defaults -- see the
[TOML Config File](#toml-config-file) section for the full list of keys.

### CLI Flags

| Flag | Description |
|------|-------------|
| `--specs-dir PATH` | Path to zwave-js/specs checkout |
| `--cache-dir PATH` | Cache directory (default: `<specs-dir>/.cache`) |
| `--app-layer-rst-dir PATH` | RST source directory for application layer spec (alternative to PDF) |
| `--config PATH` | Path to TOML configuration file |
| `--clear-cache` | Clear cache before starting |
| `--write-gitignore` | Build cache and write `.cache/.gitignore` to track pre-built blobs, then exit |

### TOML Config File

Pass a TOML file with `--config path/to/zwave-specs-mcp.toml`. All keys are
optional; only specified values override the defaults.

```toml
# Base directories
specs_dir = "~/projects/specs"
cache_dir = "/custom/cache/path"  # .cache/ is appended automatically

# RST source directory (alternative to app layer PDF)
# app_layer_rst_dir = "~/projects/rst-source/source"

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
- `ZWAVE_SPECS_MCP_APP_LAYER_RST_DIR` -- RST source directory (alternative to PDF)

Individual path overrides use the `ZWAVE_SPECS_MCP_` prefix with the key name in
uppercase:

```bash
export ZWAVE_SPECS_MCP_APP_LAYER_PDF="Z-Wave Specification AWG V5.0.pdf"
export ZWAVE_SPECS_MCP_HEADER_FILE="API_includes/ZW_classcmd.h"
```

Category dict entries use a double underscore to separate the group name
from the key:

```bash
export ZWAVE_SPECS_MCP_LEGACY_PDFS__LEGACY_APP_LAYER_V4="Z-Wave Specification AWG V4.0.pdf"
export ZWAVE_SPECS_MCP_TEST_PDFS__TEST_SECURITY="Z-Wave Security Test Specification.pdf"
```

## MCP Tools Reference

The server exposes 20 tools. Parameters marked with `| None` accept `null`
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
| `search` | `str \| None` | Search by type name (e.g., `"Smoke"`) or event text (e.g., `"intrusion"`). Omit to list all. |

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
| `search` | `str \| None` | Search text. Searches within `pdf` if provided, otherwise searches across all test specs. |

#### get_legacy_spec

Legacy Z-Wave specifications.

| Parameter | Type | Description |
|-----------|------|-------------|
| `pdf` | `str \| None` | Legacy spec key (e.g., `"legacy_500_app_guide"`). Omit to list available. |
| `section` | `str \| None` | Section title to retrieve (requires `pdf`) |
| `search` | `str \| None` | Search text. Searches within `pdf` if provided, otherwise searches across all legacy specs. |

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

### Cache Management Tools

#### rebuild_cache

Clear the spec cache and rebuild it from scratch in the background.
Cancels any in-progress cache warming, clears all cached data, and starts
a fresh background extraction. Useful after updating the specs repository.
No parameters.

## Tool Examples

<details>
<summary>Click to expand representative request/response pairs</summary>

#### `list_command_classes(category="transport")`

```
# Z-Wave Command Classes

| CC Name | CC ID | Versions | Status | Category |
|---------|-------|----------|--------|----------|
| CRC-16 Encapsulation | unknown | v1 | Active | transport |
| Multi Channel | 0x60 | v3-4 | Active | transport |
| Multi Command | unknown | v1 | Active | transport |
| Security 0 (S0) | unknown | v1 | Active | transport |
| Security 2 (S2) | unknown | v1-2 | Active | transport |
| Supervision | 0x6C | v1-2 | Active | transport |
| Transport Service | 0x55 | v1-2 | Active | transport |
```

#### `get_command_class(name="Dor Lok")`

Fuzzy-matches to "Door Lock". Source attribution differs depending on
whether the server is using PDF or RST input:

**PDF source:**

```
# Door Lock Command Class, v1-4
- **CC ID**: 0x62
- **Versions**: 1, 2, 3, 4
- **Section**: 2.2.38 (pages 524-558)
- **Source**: PDF
- **File**: /path/to/specs/Z-Wave Specification AWG V5.0.pdf
- **GitHub**: https://github.com/zwave-js/specs/blob/master/Z-Wave%20Specification%20AWG%20V5.0.pdf
- **Status**: Active

---

Door Lock Command Class, version 1-2
=============================================

The Door Lock Command Class is used to operate and configure a door lock device.
... (full spec text)
```

**RST source:**

```
# Door Lock Command Class, v1-4
- **CC ID**: 0x62
- **Versions**: 1, 2, 3, 4
- **Section**: 2.2.38
- **Source**: RST
- **File**: /path/to/rst-source/source
- **Status**: Active

---

Door Lock Command Class, version 1-2
=============================================

The Door Lock Command Class is used to operate and configure a door lock device.
... (full spec text, higher fidelity from RST — no PDF extraction artifacts)
```

#### `search_command_classes(query="thermostat setpoint", max_results=3)`

```
# Search Results for 'thermostat setpoint'

## Thermostat Setpoint (0x43, v1-3)
- Section: 2.2.116
- Score: 26468.7
- Snippet: Thermostat Setpoint Command Class, version 1-2 ...

## Thermostat Mode (0x40, v1-3)
- Section: 2.2.111
- Score: 1144.1

## Thermostat Fan Mode (0x44, v1-5)
- Section: 2.2.106
- Score: 414.4
```

#### `get_cc_commands(name="Door Lock")`

```
# Door Lock Command Class (0x62)

Source: `ZW_classcmd.h`

## Commands

| Command | Opcode |
|---------|--------|
| DOOR_LOCK_OPERATION_SET_V3 | 0x01 |
| DOOR_LOCK_OPERATION_GET_V3 | 0x02 |
| DOOR_LOCK_OPERATION_REPORT_V3 | 0x03 |
| DOOR_LOCK_CONFIGURATION_SET_V3 | 0x04 |
...

## Frame Structures

### DOOR_LOCK_OPERATION_SET_V3_FRAME
| Field | Type |
|-------|------|
| cmdClass | BYTE |
| cmd | BYTE |
| doorLockMode | BYTE |
...
```

#### `lookup_manufacturer(name="Aeotec")`

```
# Manufacturers

*Filtered by: 'Aeotec' — 1 results*

| Customer | ID | Formerly know as |
|----------|-----|------------------|
| Aeotec Ltd. | 0x0371 | |
```

#### `get_lifeline_requirements(command_class="Door Lock")`

```
# Lifeline Association Commands

*Filtered by: 'Door Lock' — 2 results*

| Command Class | Command | Conditions and triggers |
|---------------|---------|------------------------|
| Door Lock | Door Lock Operation Report | ... |
| Door Lock | Notification Report | ... |
```

#### `get_spec_section(pdf="network_layer")`

Without `section` or `search`, returns a table of contents:

```
# network_layer — Table of Contents

- **1**: 1 Abbreviations (pages 11-11)
- **6**: 2.4 Network layer specification (pages 12-12)
- **7**: 2.5 Glossary (pages 13-13)
- **9**: 3.1 The Z-Wave protocol stack architecture (pages 14-15)
- **10**: 4 Z-Wave Networking (pages 16-83)
- **11**: 5 SmartStart (pages 84-102)
...
```

#### `get_spec_section(pdf="network_layer", section="SmartStart")`

```
# 5 SmartStart
- Source: `network_layer`
- **File**: /path/to/specs/Z-Wave Stack Specifications/Z-Wave and Z-Wave Long Range Network Layer Specification.pdf
- **GitHub**: https://github.com/zwave-js/specs/blob/master/...
- Pages: 84-102

---

(full section text)
```

#### `get_device_class(generic="Switch Binary")`

```
# Switch Binary (0x10)
- **Description**: Binary Switch
- **Source**: ZW_classcmd.h

## Specific Types

| Specific Type | ID | Description |
|--------------|-----|-------------|
| SPECIFIC_TYPE_NOT_USED | 0x00 | |
| SPECIFIC_TYPE_POWER_SWITCH_BINARY | 0x01 | Binary Power Switch |
| SPECIFIC_TYPE_SCENE_SWITCH_BINARY_V2 | 0x03 | Binary Scene Switch |
| SPECIFIC_TYPE_POWER_SWITCH_BINARY_V2 | 0x04 | |
```

#### `lookup_zwave_constants(search="TRANSMIT_OPTION", header="ZW_transport_api.h")`

```
# Z-Wave Constants matching 'TRANSMIT_OPTION'

*9 matches across header files*

## ZW_transport_api.h

| Define | Value | Description |
|--------|-------|-------------|
| TRANSMIT_OPTION_ACK | 0x01 | request acknowledge |
| TRANSMIT_OPTION_LOW_POWER | 0x02 | transmit at low output power |
| TRANSMIT_OPTION_AUTO_ROUTE | 0x04 | |
| TRANSMIT_OPTION_RETURN_ROUTE | 0x04 | |
| TRANSMIT_OPTION_NO_ROUTE | 0x10 | |
| TRANSMIT_OPTION_EXPLORE | 0x20 | use explore frame if needed |
...
```

#### `get_device_type()`

Lists all device type sections. When a name is provided,
source attribution shows PDF or RST:

```
# Device Types

- **Introduction** (pages 1161-1161)
- **Common Z-Wave Plus v2 Device Type Requirements** (pages 1162-1181)
- **Z-Wave Plus v2 Device Type Definition** (pages 1182-1204)
- **Actuator supporting types** (pages 1186-1194)
- **Reporting supporting Device Types** (pages 1195-1199)
- **Other Device Types** (pages 1200-1201)
- **Controlling Device Types** (pages 1202-1204)
```

#### `get_device_type(name="Thermostat")`

**PDF source:**

```
# Thermostat HVAC
- Source: PDF, Device Types
- **File**: /path/to/specs/Z-Wave Specification AWG V5.0.pdf
- **GitHub**: https://github.com/zwave-js/specs/blob/master/Z-Wave%20Specification%20AWG%20V5.0.pdf
- Pages: 1195-1196

---

(full device type spec text)
```

**RST source:**

```
# Thermostat HVAC
- Source: RST, Device Types
- **File**: /path/to/rst-source/source
- Pages: 1195-1196

---

(full device type spec text)
```

#### `search_application_notes()`

```
# Z-Wave Application Notes

- **`appnote_apl12955_z_wave_multi_channel_basics`**: Apl12955 Z Wave Multi Channel Basics (4 sections)
- **`appnote_apl12957_z_wave_battery_support_basics`**: Apl12957 Z Wave Battery Support Basics (3 sections)
- **`appnote_apl13031_z_wave_networking_basics`**: Apl13031 Z Wave Networking Basics (5 sections)
- **`appnote_apl13084_z_wave_control_application_basics`**: Apl13084 Z Wave Control Application Basics (4 sections)
- **`appnote_apl13128_z_wave_time_date_basics`**: Apl13128 Z Wave Time Date Basics (3 sections)
- **`appnote_apl13475_z_wave_development_basics`**: Apl13475 Z Wave Development Basics (5 sections)
...

Use `get_spec_section(pdf=key)` to read a specific note.
```

</details>

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
export ZWAVE_SPECS_MCP_LEGACY_PDFS__LEGACY_APP_LAYER_V4="Z-Wave Specification AWG V4.0.pdf"
```

For individual path overrides (like a different application layer PDF location):

```bash
export ZWAVE_SPECS_MCP_APP_LAYER_PDF="custom/path/to/AWG.pdf"
```

New entries are merged with the built-in defaults. Setting a key that
already exists replaces the default value.

## License

AGPL-3.0 -- see [LICENSE](./LICENSE).
