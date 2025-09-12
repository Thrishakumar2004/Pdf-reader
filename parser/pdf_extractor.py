# parser/pdf_extractor.py
import pdfplumber

class PDFExtractor:
    def __init__(self, pdf_path: str):
        self.pdf_path = pdf_path

    def extract_text_by_page(self):
        """
        Extracts text from each page and returns a list of dicts:
        [{"page": 1, "text": "..."}, {"page": 2, "text": "..."}]
        """
        text_pages = []
        with pdfplumber.open(self.pdf_path) as pdf:
            for i, page in enumerate(pdf.pages):
                text = page.extract_text() or ""
                print(f"[DEBUG] Page {i+1}: {len(text)} characters extracted")
                if len(text.strip()) == 0:
                    print(f"[WARNING] Page {i+1} may be image-based (needs OCR).")
                text_pages.append({"page": i + 1, "text": text})
        return text_pages

    def extract_full_text(self):
        """Concatenates all page text into a single string."""
        pages = self.extract_text_by_page()
        return "\n".join([p["text"] for p in pages if p["text"].strip()])

    def extract_toc_candidates(self, pages_text):
        """
        Extract candidate lines for TOC parsing (usually first 10 pages).
        Input: pages_text = list of {"page": int, "text": str}
        Returns: list of strings
        """
        toc_candidates = []
        for p in pages_text[:10]:  # first 10 pages usually contain TOC
            lines = p["text"].splitlines()
            for line in lines:
                if line.strip():  # keep only non-empty
                    toc_candidates.append(line.strip())
        print(f"[DEBUG] Extracted {len(toc_candidates)} TOC candidate lines")
        return toc_candidates
