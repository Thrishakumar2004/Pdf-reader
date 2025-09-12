# USB Power Delivery (USB PD) Specification Parsing System

## Project Overview
This project extracts, parses, and structures a **USB Power Delivery (USB PD) specification PDF** into machine-readable JSONL format.  
It also validates the parsed output against the Table of Contents (ToC) and generates a **validation report** in Excel.

The system is designed to:  
- Extract text and TOC from PDF.  
- Parse hierarchical sections with metadata.  
- Output JSONL files for TOC and sections.  
- Generate a validation XLSX report highlighting mismatches or gaps.  
- Enable easy ingestion into vector stores or LLM-based document agents.

---

## Project Structure

usb_pd_parser/
│
├── data/ # Sample PDF and output files
│ ├── usb_pd_spec.pdf
│ ├── usb_pd_spec.jsonl
│ ├── usb_pd_toc.jsonl
│ └── validation_report.xlsx
│
├── parser/ # Core parser modules
│ ├── init.py
│ ├── pdf_extractor.py # Extracts text from PDF
│ ├── toc_parser.py # Parses Table of Contents
│ ├── section_parser.py # Splits document into sections
│ └── validator.py # Validates parsed sections vs TOC
│
├── tests/ # Unit tests
│ └── test_pdf_extractor.py
│
├── main.py # Entry point for running the parser
├── requirements.txt # Python dependencies
└── README.md # Project documentation

---

## Installation

Clone the repository:

```bash
git clone https://github.com/Thrishakumar2004/Pdf-reader.git
cd Pdf-reader


Install dependencies:

pip install -r requirements.txt

Usage
1. Run the Parser
python main.py


This will:

Extract the text and TOC from the PDF.

Generate JSONL files:

usb_pd_spec.jsonl → all sections

usb_pd_toc.jsonl → Table of Contents

Produce validation_report.xlsx for TOC vs parsed sections comparison.

2. Example of Parsed Section JSONL
{"doc_title": "USB Power Delivery Specification Rev X", "section_id": "2.1.2", "title": "Power Delivery Contract Negotiation", "page": 53, "level": 3, "parent_id": "2.1", "full_path": "2.1.2 Power Delivery Contract Negotiation", "tags": ["contracts", "negotiation"]}

3. Validation Report

Highlights mismatches or gaps between TOC and parsed sections.

Saved as data/validation_report.xlsx.

Running Tests

Unit tests are provided to verify PDF extraction functionality:

pytest tests/test_pdf_extractor.py

Dependencies

pdfplumber → PDF text extraction

pandas → Excel validation reports

pytest → Unit testing

Install via:

pip install pdfplumber pandas pytest