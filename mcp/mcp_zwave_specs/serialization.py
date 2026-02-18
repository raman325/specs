"""Serialization helpers for cache storage of Z-Wave spec data."""

from __future__ import annotations

from mcp_zwave_specs.models import (
    CCCommand,
    CCHeaderData,
    CommandClassInfo,
    SpecSection,
    StructDef,
    StructField,
)


def serialize_cc(cc: CommandClassInfo) -> dict:
    """Serialize a CommandClassInfo to a dict (content stored separately)."""
    return {
        "name": cc.name,
        "section_number": cc.section_number,
        "cc_id": cc.cc_id,
        "versions": cc.versions,
        "status": cc.status,
        "page_start": cc.page_start,
        "page_end": cc.page_end,
        "category": cc.category,
    }


def deserialize_cc(data: dict, content: str = "") -> CommandClassInfo:
    """Deserialize a CommandClassInfo dict back into a dataclass."""
    return CommandClassInfo(
        name=data["name"],
        section_number=data["section_number"],
        cc_id=data.get("cc_id"),
        versions=data.get("versions", []),
        status=data.get("status", "Active"),
        page_start=data.get("page_start"),
        page_end=data.get("page_end"),
        content=content,
        category=data.get("category", ""),
    )


def serialize_spec_section(s: SpecSection) -> dict:
    """Serialize a SpecSection to a dict."""
    return {
        "title": s.title,
        "content": s.content,
        "pdf_name": s.pdf_name,
        "section_number": s.section_number,
        "page_start": s.page_start,
        "page_end": s.page_end,
    }


def serialize_header_data(hd: CCHeaderData) -> dict:
    """Serialize a CCHeaderData to a dict."""
    return {
        "name": hd.name,
        "cc_id": hd.cc_id,
        "commands": [
            {"name": c.name, "opcode": c.opcode, "cc_name": c.cc_name, "cc_id": c.cc_id}
            for c in hd.commands
        ],
        "structs": [
            {
                "name": s.name,
                "fields": [{"name": f.name, "type": f.type, "bits": f.bits} for f in s.fields],
            }
            for s in hd.structs
        ],
    }


def deserialize_header_data(data: dict) -> CCHeaderData:
    """Deserialize a CCHeaderData dict back into a dataclass."""
    commands = [CCCommand(**c) for c in data.get("commands", [])]
    structs = [
        StructDef(
            name=s["name"],
            fields=[StructField(**f) for f in s.get("fields", [])],
        )
        for s in data.get("structs", [])
    ]
    return CCHeaderData(
        name=data["name"],
        cc_id=data["cc_id"],
        commands=commands,
        structs=structs,
    )
