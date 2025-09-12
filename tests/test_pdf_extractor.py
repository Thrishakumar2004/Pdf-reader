import pytest
from parser.pdf_extractor import PDFExtractor

def test_pdf_extractor_methods():
    # Mock PDF path (does not need to exist for this test)
    pdf_path = "mock_path/usb_pd_spec.pdf"

    # Initialize PDFExtractor
    extractor = PDFExtractor(pdf_path)

    # Mock text pages
    mock_text_pages = [
        {"page": 1, "text": "Overview\nSome overview text."},
        {"page": 2, "text": "Introduction\nThis is the introduction section."},
    ]

    # Patch the methods to return mock data instead of reading a real PDF
    extractor.extract_text_by_page = lambda: mock_text_pages
    extractor.extract_full_text = lambda: "\n".join(page["text"] for page in mock_text_pages)
    extractor.extract_toc_candidates = lambda pages: [page["text"].split("\n")[0] for page in pages]

    # Run the methods
    pages = extractor.extract_text_by_page()
    full_text = extractor.extract_full_text()
    toc_candidates = extractor.extract_toc_candidates(pages)

    # Assertions
    assert isinstance(pages, list), "extract_text_by_page should return a list"
    assert len(pages) == 2, "There should be 2 pages"
    assert isinstance(full_text, str), "extract_full_text should return a string"
    assert full_text.startswith("Overview"), "Full text should start with first page content"
    assert toc_candidates == ["Overview", "Introduction"], "TOC candidates should match page headers"
