"""Parse ZW_classcmd.h and other Z-Wave C headers for structured data."""

from __future__ import annotations

import logging
import re
from dataclasses import dataclass, field
from pathlib import Path

from mcp_zwave_specs.models import CCCommand, CCHeaderData, StructDef, StructField

logger = logging.getLogger(__name__)

# Matches: #define COMMAND_CLASS_FOO_BAR  0x71 /*[DEPRECATED]*/
RE_CC_DEFINE = re.compile(
    r"^#define\s+(COMMAND_CLASS_\w+)\s+(0x[0-9A-Fa-f]+)\s*(?:/\*\[(\w+)\]\*/)?",
    re.MULTILINE,
)

# Matches section comment: /* Foo Bar command class commands */
RE_CC_SECTION = re.compile(r"^/\*\s*(.+?)\s+command class commands\s*\*/", re.MULTILINE)

# Matches: #define FOO_BAR_V2  0x04
RE_OPCODE = re.compile(
    r"^#define\s+(\w+)\s+(0x[0-9A-Fa-f]+)",
    re.MULTILINE,
)

# Matches: /* Values used for ... */
RE_VALUES_COMMENT = re.compile(r"^/\*\s*Values used for", re.MULTILINE)

# Matches: /* Foo Bar Get V2 command class structs */
RE_STRUCT_SECTION = re.compile(r"^/\*\s*(.+?)\s+command class structs\s*\*/", re.MULTILINE)

# Matches typedef struct blocks
RE_STRUCT = re.compile(
    r"typedef\s+struct\s+\w+\s*\{([^}]+)\}\s*(\w+)\s*;",
    re.DOTALL,
)

# Matches struct field: BYTE  fieldName;  /* comment */
RE_FIELD = re.compile(r"(\w+)\s+(\w+)\s*;")


def _normalize_cc_name(raw: str) -> str:
    """COMMAND_CLASS_DOOR_LOCK_V4 → Door Lock."""
    name = raw.removeprefix("COMMAND_CLASS_")
    name = re.sub(r"_V\d+$", "", name)
    return name.replace("_", " ").title()


def _parse_cc_defines(text: str) -> dict[str, int]:
    """Extract CC name → ID mapping, deduplicating versioned entries."""
    cc_map: dict[str, int] = {}
    for m in RE_CC_DEFINE.finditer(text):
        raw_name = m.group(1)
        cc_id = int(m.group(2), 16)
        normalized = _normalize_cc_name(raw_name)
        # First occurrence wins (unversioned or lowest version)
        if normalized not in cc_map:
            cc_map[normalized] = cc_id
    return cc_map


def _parse_command_sections(text: str) -> dict[str, list[CCCommand]]:
    """Parse command opcodes grouped by CC section comments."""
    commands_by_cc: dict[str, list[CCCommand]] = {}

    section_starts = list(RE_CC_SECTION.finditer(text))
    for i, match in enumerate(section_starts):
        section_name = match.group(1).strip()
        # Normalize: "Alarm" → "Alarm", "Notification V3" → "Notification"
        base_name = re.sub(r"\s+V\d+$", "", section_name).title()

        start = match.end()
        end = section_starts[i + 1].start() if i + 1 < len(section_starts) else len(text)
        section_text = text[start:end]

        # Find opcodes: defines between VERSION and "Values used for" comments
        values_match = RE_VALUES_COMMENT.search(section_text)
        opcode_region = section_text[: values_match.start()] if values_match else section_text

        commands = []
        for op_match in RE_OPCODE.finditer(opcode_region):
            name = op_match.group(1)
            value = int(op_match.group(2), 16)
            # Skip VERSION defines and PROPERTIES/MASK/SHIFT constants
            if "_VERSION" in name:
                continue
            if any(x in name for x in ("_MASK", "_SHIFT", "_RESERVED", "_PROPERTIES")):
                continue
            commands.append(CCCommand(name=name, opcode=value, cc_name=base_name, cc_id=0))

        if commands:
            commands_by_cc.setdefault(base_name, []).extend(commands)

    return commands_by_cc


def _cc_name_from_struct_comment(comment: str) -> str:
    """Extract CC base name from struct section comment.

    'Alarm Get V2' → 'Alarm'
    'Door Lock Operation Set V3' → 'Door Lock'
    'Notification Report 1byte V5' → 'Notification'
    """
    # Remove version suffix, byte counts, and command names
    name = re.sub(r"\s+V\d+$", "", comment)
    name = re.sub(r"\s+\d+byte$", "", name, flags=re.IGNORECASE)
    # Remove trailing command words (Get, Set, Report, Supported, etc.)
    command_words = {
        "Get",
        "Set",
        "Report",
        "Supported",
        "Configuration",
        "Operation",
        "Notification",
        "Type",
        "Event",
        "Capabilities",
    }
    parts = name.split()
    # Walk backwards removing known command suffixes, but keep at least one word
    while len(parts) > 1 and parts[-1] in command_words:
        parts.pop()
    return " ".join(parts).title()


def _parse_structs(text: str, known_cc_names: set[str]) -> dict[str, list[StructDef]]:
    """Parse typedef struct blocks, grouped by CC name using section comments."""
    structs_by_cc: dict[str, list[StructDef]] = {}

    # Find struct section comments and the structs that follow them
    section_matches = list(RE_STRUCT_SECTION.finditer(text))

    for i, sec_match in enumerate(section_matches):
        raw_name = sec_match.group(1).strip()
        cc_name = _cc_name_from_struct_comment(raw_name)

        # If the derived name doesn't match any known CC, try prefix matching
        if cc_name not in known_cc_names:
            for known in known_cc_names:
                if cc_name.startswith(known):
                    cc_name = known
                    break

        start = sec_match.end()
        end = section_matches[i + 1].start() if i + 1 < len(section_matches) else len(text)
        region = text[start:end]

        for m in RE_STRUCT.finditer(region):
            body = m.group(1)
            struct_name = m.group(2)
            fields = [
                StructField(name=fm.group(2), type=fm.group(1)) for fm in RE_FIELD.finditer(body)
            ]
            if fields:
                structs_by_cc.setdefault(cc_name, []).append(
                    StructDef(name=struct_name, fields=fields)
                )

    return structs_by_cc


def parse_header(header_path: Path) -> dict[str, CCHeaderData]:
    """Parse ZW_classcmd.h and return CCHeaderData per command class."""
    text = header_path.read_text(encoding="utf-8", errors="replace")

    cc_ids = _parse_cc_defines(text)
    commands_by_cc = _parse_command_sections(text)
    known_names = set(cc_ids) | set(commands_by_cc)
    structs_by_cc = _parse_structs(text, known_names)

    all_cc_names = known_names | set(structs_by_cc)
    result: dict[str, CCHeaderData] = {}

    for name in sorted(all_cc_names):
        cc_id = cc_ids.get(name, 0)
        commands = commands_by_cc.get(name, [])
        # Backfill cc_id into commands
        for cmd in commands:
            cmd.cc_id = cc_id
        # Deduplicate commands by opcode (keep latest version's name)
        seen_opcodes: dict[int, CCCommand] = {}
        for cmd in commands:
            seen_opcodes[cmd.opcode] = cmd
        deduped = list(seen_opcodes.values())

        structs = structs_by_cc.get(name, [])
        result[name] = CCHeaderData(name=name, cc_id=cc_id, commands=deduped, structs=structs)

    logger.info("Parsed %d command classes from header", len(result))
    return result


# --- Device Class Parsing ---

# Matches: /* Device class Foo Bar */
RE_DEVICE_CLASS_COMMENT = re.compile(r"^/\*\s*Device class\s+(.+?)\s*\*/", re.MULTILINE)

RE_GENERIC_TYPE = re.compile(
    r"^#define\s+GENERIC_TYPE_(\w+)\s+(0x[0-9A-Fa-f]+)\s*(?:/\*(.+?)\*/)?",
    re.MULTILINE,
)
RE_SPECIFIC_TYPE = re.compile(
    r"^#define\s+SPECIFIC_TYPE_(\w+)\s+(0x[0-9A-Fa-f]+)\s*(?:/\*(.+?)\*/)?",
    re.MULTILINE,
)


@dataclass
class DeviceClass:
    """A generic device class with its specific subtypes."""

    generic_name: str
    generic_id: int
    comment: str = ""
    specific_types: list[tuple[str, int, str]] = field(default_factory=list)  # (name, id, comment)


def parse_device_classes(header_path: Path) -> list[DeviceClass]:
    """Parse GENERIC_TYPE/SPECIFIC_TYPE from ZW_classcmd.h."""
    text = header_path.read_text(encoding="utf-8", errors="replace")

    # Find the device class section
    marker = "Generic and Specific Device Class identifiers"
    start_idx = text.find(marker)
    if start_idx < 0:
        logger.warning("Device class section not found in header")
        return []

    device_text = text[start_idx:]
    classes: list[DeviceClass] = []
    current: DeviceClass | None = None

    for line in device_text.splitlines():
        gm = RE_GENERIC_TYPE.match(line)
        if gm:
            raw_name = gm.group(1).replace("_", " ").title()
            gid = int(gm.group(2), 16)
            comment = gm.group(3).strip() if gm.group(3) else ""
            current = DeviceClass(generic_name=raw_name, generic_id=gid, comment=comment)
            classes.append(current)
            continue

        sm = RE_SPECIFIC_TYPE.match(line)
        if sm and current is not None:
            raw_name = sm.group(1).replace("_", " ").title()
            sid = int(sm.group(2), 16)
            comment = sm.group(3).strip() if sm.group(3) else ""
            if raw_name != "Not Used":
                current.specific_types.append((raw_name, sid, comment))

    logger.info("Parsed %d generic device classes", len(classes))
    return classes


# --- Generic Header Constants Parsing ---


@dataclass
class HeaderConstant:
    """A #define constant from a header file."""

    name: str
    value: str
    comment: str = ""


def parse_header_constants(
    header_path: Path,
    prefix_filter: str | None = None,
) -> list[HeaderConstant]:
    """Parse #define constants from any header file.

    Args:
        header_path: Path to the .h file.
        prefix_filter: Only include defines starting with this prefix.
    """
    text = header_path.read_text(encoding="utf-8", errors="replace")
    pattern = re.compile(
        r"^#define\s+(\w+)\s+(0x[0-9A-Fa-f]+|\d+)\s*(?:/\*(.+?)\*/)?",
        re.MULTILINE,
    )

    constants: list[HeaderConstant] = []
    for m in pattern.finditer(text):
        name = m.group(1)
        if prefix_filter and not name.startswith(prefix_filter):
            continue
        value = m.group(2)
        comment = m.group(3).strip() if m.group(3) else ""
        constants.append(HeaderConstant(name=name, value=value, comment=comment))

    logger.info("Parsed %d constants from %s", len(constants), header_path.name)
    return constants
