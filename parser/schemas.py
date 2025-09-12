# parser/schemas.py

toc_entry_schema = {
    "type": "object",
    "properties": {
        "section": {"type": "string"},
        "title": {"type": "string"},
        "page": {"type": "integer"},
    },
    "required": ["section", "title", "page"],
}

section_entry_schema = {
    "type": "object",
    "properties": {
        "section": {"type": "string"},
        "title": {"type": "string"},
        "content": {"type": "string"},
        "start_page": {"type": "integer"},
        "end_page": {"type": ["integer", "null"]},
    },
    "required": ["section", "title", "content", "start_page"],
}
