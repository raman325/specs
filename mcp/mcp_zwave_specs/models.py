"""Data models for Z-Wave specification data."""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class CommandClassInfo:
    """A Command Class extracted from the application layer spec."""

    name: str
    section_number: str  # e.g., "2.2.37"
    cc_id: int | None = None  # e.g., 0x62
    versions: list[int] = field(default_factory=list)  # e.g., [1, 2, 3, 4]
    status: str = "Active"  # Active, DEPRECATED, OBSOLETE
    page_start: int | None = None
    page_end: int | None = None
    content: str = ""  # Full markdown text of the section
    category: str = ""  # "application", "management", "transport", etc.

    @property
    def id_hex(self) -> str:
        return f"0x{self.cc_id:02X}" if self.cc_id is not None else "unknown"

    @property
    def version_str(self) -> str:
        if not self.versions:
            return ""
        if len(self.versions) == 1:
            return f"v{self.versions[0]}"
        return f"v{self.versions[0]}-{self.versions[-1]}"


@dataclass
class CCCommand:
    """A single command within a Command Class, parsed from ZW_classcmd.h."""

    name: str
    opcode: int
    cc_name: str
    cc_id: int

    @property
    def opcode_hex(self) -> str:
        return f"0x{self.opcode:02X}"


@dataclass
class StructField:
    """A field within a frame struct definition."""

    name: str
    type: str
    bits: int | None = None


@dataclass
class StructDef:
    """A typedef struct from ZW_classcmd.h representing a command frame."""

    name: str
    fields: list[StructField] = field(default_factory=list)


@dataclass
class CCHeaderData:
    """All data parsed from ZW_classcmd.h for a single Command Class."""

    name: str
    cc_id: int
    commands: list[CCCommand] = field(default_factory=list)
    structs: list[StructDef] = field(default_factory=list)

    @property
    def id_hex(self) -> str:
        return f"0x{self.cc_id:02X}"


@dataclass
class SpecSection:
    """A section from a supplementary (non-CC) spec PDF."""

    title: str
    content: str
    pdf_name: str
    section_number: str = ""
    page_start: int | None = None
    page_end: int | None = None


@dataclass
class RegistryData:
    """Parsed data from a registry Excel file."""

    name: str  # Human-readable name, e.g., "Notification Types"
    filename: str  # Original xlsx filename
    rows: list[dict[str, str]] = field(default_factory=list)
    columns: list[str] = field(default_factory=list)
