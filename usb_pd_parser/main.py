import pdfplumber
import re
import json
import pandas as pd  # For Excel export

# ------------------ Step 1: Extract text ------------------
def extract_pdf_text(pdf_path, start_page=0, end_page=None):
    text_by_page = []
    with pdfplumber.open(pdf_path) as pdf:
        if end_page is None:
            end_page = len(pdf.pages)
        for i in range(start_page, end_page):
            page = pdf.pages[i]
            text = page.extract_text() or ""
            text_by_page.append(text)
            print(f"✅ Processed page {i+1}/{len(pdf.pages)}")
    return text_by_page

# ------------------ Step 2: Parse TOC ------------------
def parse_toc(toc_lines, doc_title):
    toc_pattern = re.compile(r"^(\d+(?:\.\d+)*?)\s+(.+?)\s+(\d+)$")
    result = []
    for line in toc_lines:
        match = toc_pattern.match(line.strip())
        if match:
            section_id = match.group(1)
            title = match.group(2).strip()
            page = int(match.group(3))
            level = section_id.count('.') + 1
            parent_id = '.'.join(section_id.split('.')[:-1]) if '.' in section_id else None
            result.append({
                "doc_title": doc_title,
                "section_id": section_id,
                "title": title,
                "full_path": f"{section_id} {title}",
                "page": page,
                "level": level,
                "parent_id": parent_id,
                "tags": []
            })
    return result

# ------------------ Save JSONL ------------------
def save_jsonl(data, filename):
    with open(filename, "w", encoding="utf-8") as f:
        for entry in data:
            f.write(json.dumps(entry) + "\n")

# ------------------ Step 3: Parse document sections ------------------
def parse_sections(all_pages_text, doc_title):
    section_pattern = re.compile(r"^(\d+(?:\.\d+)*?)\s+(.+)$")
    result = []
    for page_num, page_text in enumerate(all_pages_text, start=1):
        for line in page_text.split("\n"):
            match = section_pattern.match(line.strip())
            if match:
                section_id = match.group(1)
                title = match.group(2).strip()
                level = section_id.count('.') + 1
                parent_id = '.'.join(section_id.split('.')[:-1]) if '.' in section_id else None
                result.append({
                    "doc_title": doc_title,
                    "section_id": section_id,
                    "title": title,
                    "full_path": f"{section_id} {title}",
                    "page": page_num,
                    "level": level,
                    "parent_id": parent_id,
                    "tags": []
                })
    return result

# ------------------ Step 4: Extract section content ------------------
def extract_sections_content(toc_data, all_pages_text):
    sections_content = []
    for i, toc_entry in enumerate(toc_data):
        start_page = toc_entry['page'] - 1
        if i + 1 < len(toc_data):
            end_page = toc_data[i + 1]['page'] - 1
        else:
            end_page = len(all_pages_text)
        content = "\n".join(all_pages_text[start_page:end_page])
        sections_content.append({
            **toc_entry,
            "content": content.strip()
        })
    return sections_content

# ------------------ Step 5: Save to Excel ------------------
def save_to_excel(data, filename):
    df = pd.DataFrame(data)
    df.to_excel(filename, index=False)
    print(f"Excel file saved: {filename}")

# ------------------ Main Runner ------------------
if __name__ == "__main__":
    pdf_file = "C:/Users/Thrisha/Desktop/usb_pd_parser/usb_pd_specification.pdf"
    doc_title = "USB Power Delivery Specification"

    # Extract ALL text from PDF
    all_text = extract_pdf_text(pdf_file)

    # OPTIONAL: Preview first 20 pages
    for i, text in enumerate(all_text[:20]):
        print(f"\n--- Page {i+1} ---\n{text}\n")

    # Parse TOC (adjust range if TOC spans more than 3 pages)
    toc_text = []
    for p in range(0, 3):
        toc_text.extend(all_text[p].split("\n"))
    toc_data = parse_toc(toc_text, doc_title)

    for entry in toc_data:
        print(f"{entry['section_id']}: {entry['title']} .......... {entry['page']}")

    save_jsonl(toc_data, "usb_pd_toc.jsonl")
    print(f"TOC entries extracted: {len(toc_data)}")

    # Parse document sections
    sections_data = parse_sections(all_text, doc_title)
    save_jsonl(sections_data, "usb_pd_spec.jsonl")
    print(f"Document sections extracted: {len(sections_data)}")

    # Extract content for each TOC section
    sections_with_content = extract_sections_content(toc_data, all_text)
    save_jsonl(sections_with_content, "usb_pd_sections_with_content.jsonl")
    print(f"Sections with content extracted: {len(sections_with_content)}")

    # Save to Excel
    save_to_excel(sections_with_content, "usb_pd_sections_with_content.xlsx")
