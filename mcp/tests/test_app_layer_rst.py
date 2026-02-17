"""Tests for RST source extractor."""


import pytest

from mcp_zwave_specs.extractors.app_layer_rst import (
    RE_CC_RST,
    _parse_toctree,
    extract_app_layer_chapter_sections_rst,
    split_app_layer_sections_rst,
)

# --- RE_CC_RST regex ---


@pytest.mark.parametrize(
    "title, expected_name, expected_start, expected_end, expected_status",
    [
        ("Door Lock Command Class, version 4", "Door Lock", 4, None, None),
        ("Alarm Command Class, version 1", "Alarm", 1, None, None),
        ("Door Lock Command Class, version 1-2", "Door Lock", 1, 2, None),
        (
            "Multilevel Sensor Command Class, version 5-11",
            "Multilevel Sensor",
            5,
            11,
            None,
        ),
        (
            "Alarm Command Class, version 1 [DEPRECATED]",
            "Alarm",
            1,
            None,
            "DEPRECATED",
        ),
        (
            "Binary Switch Command Class, version 1-2 [OBSOLETE]",
            "Binary Switch",
            1,
            2,
            "OBSOLETE",
        ),
    ],
)
def test_re_cc_rst(title, expected_name, expected_start, expected_end, expected_status):
    m = RE_CC_RST.match(title)
    assert m is not None
    assert m.group(1).strip() == expected_name
    assert int(m.group(2)) == expected_start
    assert m.group(3) == (str(expected_end) if expected_end else None)
    assert m.group(4) == expected_status


# --- _parse_toctree ---


def test_parse_toctree(tmp_path):
    rst = tmp_path / "index.rst"
    rst.write_text(
        "Title\n=====\n\n"
        ".. toctree::\n"
        "  :maxdepth: 5\n\n"
        "  First Section <first.rst>\n"
        "  Second Section <subdir/second.rst>\n"
    )
    (tmp_path / "first.rst").write_text("content")
    sub = tmp_path / "subdir"
    sub.mkdir()
    (sub / "second.rst").write_text("content")

    entries = _parse_toctree(rst)
    assert len(entries) == 2
    assert entries[0][0] == "First Section"
    assert entries[0][1] == (tmp_path / "first.rst").resolve()
    assert entries[1][0] == "Second Section"
    assert entries[1][1] == (sub / "second.rst").resolve()


def test_parse_toctree_adds_rst_extension(tmp_path):
    rst = tmp_path / "index.rst"
    rst.write_text(".. toctree::\n\n  My Page <my_page>\n")
    entries = _parse_toctree(rst)
    assert len(entries) == 1
    assert entries[0][1].name == "my_page.rst"


# --- split_app_layer_sections_rst ---


def _build_rst_tree(tmp_path):
    """Build a minimal RST source tree for testing."""
    # application_command_classes
    app_dir = tmp_path / "application_command_classes"
    app_dir.mkdir()
    cc_dir = app_dir / "command_class_definitions"
    cc_dir.mkdir()

    (app_dir / "command_class_definitions.rst").write_text(
        "Definitions\n===========\n\n"
        ".. toctree::\n"
        "  :maxdepth: 5\n\n"
        "  Basic Command Class, version 1 <command_class_definitions/basic_v1.rst>\n"
        "  Basic Command Class, version 2 <command_class_definitions/basic_v2.rst>\n"
        "  Door Lock Command Class, version 1-2 <command_class_definitions/door_lock_v1_2.rst>\n"
    )
    (cc_dir / "basic_v1.rst").write_text("Basic CC v1 content")
    (cc_dir / "basic_v2.rst").write_text("Basic CC v2 content")
    (cc_dir / "door_lock_v1_2.rst").write_text("Door Lock CC v1-2 content")

    # management_command_classes (empty — should be skipped gracefully)
    mgmt_dir = tmp_path / "management_command_classes"
    mgmt_dir.mkdir()

    return tmp_path


def test_split_app_layer_sections_rst(tmp_path):
    rst_dir = _build_rst_tree(tmp_path)
    sections = split_app_layer_sections_rst(rst_dir)

    assert len(sections) == 3

    basic_v1 = sections[0]
    assert basic_v1.name == "Basic"
    assert basic_v1.versions == [1]
    assert basic_v1.category == "application"
    assert "Basic CC v1 content" in basic_v1.content

    basic_v2 = sections[1]
    assert basic_v2.name == "Basic"
    assert basic_v2.versions == [2]

    door_lock = sections[2]
    assert door_lock.name == "Door Lock"
    assert door_lock.versions == [1, 2]
    assert "Door Lock CC v1-2 content" in door_lock.content


def test_split_app_layer_sections_rst_section_numbers(tmp_path):
    rst_dir = _build_rst_tree(tmp_path)
    sections = split_app_layer_sections_rst(rst_dir)

    # Application chapter uses "2.2" prefix
    assert sections[0].section_number == "2.2.1"
    assert sections[1].section_number == "2.2.2"
    assert sections[2].section_number == "2.2.3"


# --- extract_app_layer_chapter_sections_rst ---


def test_extract_chapter_sections_rst(tmp_path):
    # Build a role_type chapter
    role_dir = tmp_path / "role_type"
    role_dir.mkdir()
    (role_dir / "index.rst").write_text(
        "Role Type\n=========\n\n"
        ".. toctree::\n\n"
        "  Introduction <intro.rst>\n"
        "  Definitions <defs.rst>\n"
    )
    (role_dir / "intro.rst").write_text("Role type intro")
    (role_dir / "defs.rst").write_text("Role type definitions")

    result = extract_app_layer_chapter_sections_rst(tmp_path)
    assert "role_types" in result
    sections = result["role_types"]
    assert len(sections) == 2
    assert sections[0].title == "Introduction"
    assert sections[0].pdf_name == "app_layer"
    assert "Role type intro" in sections[0].content
    assert sections[1].title == "Definitions"
