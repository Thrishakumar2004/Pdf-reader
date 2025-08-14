# USB PD Specification PDF Parser

This project extracts, parses, and structures content from the **USB Power Delivery Specification PDF**.  
It outputs:
- Table of Contents (TOC)
- Document sections
- Section content  
All outputs are available in both **JSONL** and **Excel** formats.

---

## 📌 Features
- 📄 Extracts text from PDF using `pdfplumber`
- 🗂 Parses Table of Contents into a structured JSONL file
- 🔍 Extracts document sections with section IDs and titles
- 📑 Captures full section content and saves as JSONL & Excel
- ⚡ Customizable page ranges for faster processing

---

## 📂 Project Structure
usb_pd_parser/
├── main.py # Main runner script
├── usb_pd_specification.pdf # Input PDF (not included in repo)
├── usb_pd_toc.jsonl # Extracted Table of Contents
├── usb_pd_spec.jsonl # Parsed document sections
├── usb_pd_sections_with_content.jsonl # Sections with content
├── usb_pd_sections_with_content.xlsx # Excel export


---

## 🛠 Installation
Install dependencies:
```bash
pip install pdfplumber pandas

---

## 🚀 Usage
Place your usb_pd_specification.pdf file in the project directory.

Run the script:
python main.py

---

## Outputs:
usb_pd_toc.jsonl — Parsed Table of Contents
usb_pd_spec.jsonl — Parsed document sections
usb_pd_sections_with_content.jsonl — Section content
usb_pd_sections_with_content.xlsx — Excel version

---
## 📄 Example TOC Output
usb_pd_toc.jsonl
{
    "doc_title": "USB Power Delivery Specification",
    "section_id": "1.1",
    "title": "Scope",
    "full_path": "1.1 Scope",
    "page": 5,
    "level": 2,
    "parent_id": "1",
    "tags": []
}
---
##📊 Excel Output
The .xlsx file contains:
Section ID
Title
Page number
Full section content
---
