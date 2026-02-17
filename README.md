# Z-Wave Specifications + MCP Server

This repository contains the Z-Wave specification documents from
[zwave-js/specs](https://github.com/zwave-js/specs) along with an MCP
(Model Context Protocol) server that makes those specifications queryable
by LLMs.

## Repository Structure

```
.
├── Z-Wave Command Classes Specifications/   # CC spec PDFs and CC list spreadsheet
├── Z-Wave Stack Specifications/             # Network layer, Host API, PHY/MAC specs
├── Z-Wave Plus v2 Specifications/           # Z-Wave Plus v2 device type specs
├── Z-Wave Device and Command Class Definition Files/
├── SmartStart Specifications/               # SmartStart provisioning specs
├── Legacy Specifications/                   # Older 500-series and v1 specs
├── Application Notes/                       # APL/INS application notes
├── Registries/                              # Notification types, sensor types, etc.
├── API_includes/                            # C header files (ZW_classcmd.h, etc.)
├── Z-Wave Specification AWG V5.0.pdf        # Application Workgroup spec (main CC document)
├── mcp/                                     # MCP server Python package
│   ├── mcp_zwave_specs/                     # Package source
│   ├── tests/                               # Test suite
│   └── README.md                            # Installation, configuration, and usage
└── LICENSE                                  # AGPL-3.0
```

## MCP Server

The `mcp/` directory contains a Python MCP server (`zwave-specs-mcp`) that
parses, caches, and serves the Z-Wave specifications for LLMS to query.

See [mcp/README.md](mcp/README.md) for installation,
configuration, and full tool reference.
