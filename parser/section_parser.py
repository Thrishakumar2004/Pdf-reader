# parser/section_parser.py
import re
import json

class SectionParser:
    def __init__(self, doc_title=None):
        self.doc_title = doc_title

    def split_sections(self, text_pages, toc_entries):
        """
        Splits the full document text into sections based on TOC entries.
        Each section is bounded by its starting page_number and the next entry's page_number.
        """
        sections = []

        toc_entries = sorted(toc_entries, key=lambda x: x["page_number"])

        for i, entry in enumerate(toc_entries):
            start = entry["page_number"]
            end = toc_entries[i + 1]["page_number"] if i + 1 < len(toc_entries) else None
            section_text = self._extract_section_text(text_pages, start, end)

            section_data = {
                "doc_title": self.doc_title,
                "section_id": entry["section_id"],
                "title": entry["title"],
                "page_number": entry["page_number"],
                "level": entry.get("level", None),
                "parent_id": entry.get("parent_id", None),
                "full_path": f"{entry['section_id']} {entry['title']}",
                "content": section_text.strip()
            }

            print(f"[DEBUG] Section added → {section_data['section_id']} | Page {start}")

            sections.append(section_data)

        return sections

    def _extract_section_text(self, text_pages, start_page, end_page=None):
        """
        Extracts text between start_page and end_page.
        If end_page is None, extract till the end of the document.
        """
        extracted = []
        for page in text_pages:
            if page["page"] >= start_page and (end_page is None or page["page"] < end_page):
                extracted.append(page["text"])
        return "\n".join(extracted)

    def save_to_jsonl(self, sections, path: str):
        """Save sections to a JSONL file."""
        with open(path, "w", encoding="utf-8") as f:
            for sec in sections:
                f.write(json.dumps(sec, ensure_ascii=False) + "\n")
