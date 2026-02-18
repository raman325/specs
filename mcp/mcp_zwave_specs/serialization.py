"""Serialization helpers for cache storage of Z-Wave spec data."""

from __future__ import annotations

from mcp_zwave_specs.models import (
    CCCommand,
    CCHeaderData,
    CommandClassInfo,
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
