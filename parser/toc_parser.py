# parser/toc_parser.py
import re
import json

class TOCParser:
    def __init__(self, doc_title=None):
        self.doc_title = doc_title

    def parse_toc(self, lines):
        """
        Parses Table of Contents lines into structured entries.
        """
        entries = []
        patterns = [
            r"^\s*(\d+(?:\.\d+)*)\s+(.+?)\s+(\d+)\s*$",  # e.g., 2.1.3 Title ..... 45
            r"^\s*(\d+)\s+(.+?)\s+(\d+)\s*$",             # e.g., 12 Title ..... 120
        ]
        for line in lines:
            matched = False
            for pattern in patterns:
                match = re.match(pattern, line)
                if match:
                    section_id = match.group(1)
                    title = match.group(2).strip()
                    page = int(match.group(3))
                    entries.append({
                        "doc_title": self.doc_title,
                        "section_id": section_id,
                        "title": title,
                        "page_number": page
                    })
                    print(f"[DEBUG] TOC match → {section_id} | {title} | {page}")
                    matched = True
                    break
            if not matched:
                print(f"[DEBUG] TOC no match: {line}")
        return entries

    def save_to_jsonl(self, entries, path: str):
        with open(path, "w", encoding="utf-8") as f:
            for entry in entries:
                f.write(json.dumps(entry) + "\n")
