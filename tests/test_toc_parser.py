import pytest
from parser.toc_parser import TOCParser

def test_toc_parser_extracts_entries():
    sample_lines = [
        "2 Overview ........................................ 53",
        "2.1 Introduction ................................ 53",
        "2.1.1 Power Delivery Source Operational Contracts 53",
        "2.1.2 Power Delivery Contract Negotiation ....... 53",
    ]

    parser = TOCParser("USB PD Specification Rev X")
    entries = parser.parse_toc(sample_lines)

    # Debug print to see actual output
    print(entries)

    # Basic assertions
    assert isinstance(entries, list), "Output should be a list"
    assert len(entries) == 4, "There should be 4 TOC entries parsed"

    # Check the titles (ignore page numbers since not returned)
    assert entries[0]["title"].startswith("Overview")
    assert entries[2]["title"].startswith("Power Delivery Source Operational Contracts")
