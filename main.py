"""
Main entry point for USB PD Specification Parsing System.
Runs PDF extraction, TOC parsing, section parsing, and validation.
"""

from parser.pdf_extractor import PDFExtractor
from parser.toc_parser import TOCParser
from parser.section_parser import SectionParser
from parser.validator import Validator  # Use the Validator you provided

def main():
    pdf_path = "data/usb_pd_spec.pdf"  # Path to your PDF file
    doc_title = "USB Power Delivery Specification Rev X"

    # Step 1: Extract text from PDF
    extractor = PDFExtractor(pdf_path)
    text_pages = extractor.extract_text_by_page()  # List of {"page": 1, "text": "..."}
    full_text = extractor.extract_full_text()      # Optional: full text as single string

    # Step 2: Extract TOC candidates and parse TOC
    toc_text = extractor.extract_toc_candidates(text_pages)
    toc_parser = TOCParser(doc_title)
    toc_entries = toc_parser.parse_toc(toc_text)
    toc_parser.save_to_jsonl(toc_entries, "data/usb_pd_toc.jsonl")
    print(f"[INFO] Saved TOC JSONL with {len(toc_entries)} entries.")

    # Step 3: Parse sections using TOC
    section_parser = SectionParser(doc_title)
    section_entries = section_parser.split_sections(text_pages, toc_entries)
    section_parser.save_to_jsonl(section_entries, "data/usb_pd_spec.jsonl")
    print(f"[INFO] Saved sections JSONL with {len(section_entries)} entries.")

    # Step 4: Validation using Validator class
    Validator.generate_report(toc_entries, section_entries, "data/validation_report.xlsx")
    print("[INFO] Validation completed. Report saved to data/validation_report.xlsx")

if __name__ == "__main__":
    main()
