import pytest
from parser.section_parser import SectionParser
from parser.toc_parser import TOCParser

def test_section_parser_splits_sections():
    # Mock text pages as list of dictionaries
    text_pages = [
        {"page": 1, "text": "Overview\nSome overview text here."},
        {"page": 2, "text": "Introduction\nThis is the introduction section."},
        {"page": 3, "text": "Power Delivery Source Operational Contracts\nDetails about power delivery source."},
        {"page": 4, "text": "Power Delivery Contract Negotiation\nNegotiation details here."},
    ]

    # Mock TOC lines
    toc_lines = [
        "2 Overview ........................................ 1",
        "2.1 Introduction ................................ 2",
        "2.1.1 Power Delivery Source Operational Contracts 3",
        "2.1.2 Power Delivery Contract Negotiation ....... 4",
    ]

    # Initialize TOC parser and parse the TOC
    toc_parser = TOCParser("USB PD Specification Rev X")
    toc_entries = toc_parser.parse_toc(toc_lines)

    # Initialize SectionParser
    section_parser = SectionParser("USB PD Specification Rev X")
    section_entries = section_parser.split_sections(text_pages, toc_entries)

    # Debug print to inspect output
    print(section_entries)

    # Basic assertions
    assert isinstance(section_entries, list), "Output should be a list"
    assert len(section_entries) == len(toc_entries), "Number of sections should match TOC entries"

    # Check that section entries contain the title key
    for toc_entry, section_entry in zip(toc_entries, section_entries):
        assert "title" in section_entry, "Section entry must contain 'title'"
        assert section_entry["title"].startswith(toc_entry["title"].split()[0]), \
            "Section title should match TOC title"
