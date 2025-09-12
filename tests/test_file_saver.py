import os
import tempfile
import pandas as pd
import pytest
from parser.validator import Validator  # Assuming you want to test file saving via Validator

def test_generate_report_creates_excel_file():
    # Mock TOC and section entries
    toc_entries = [{"title": "Overview"}, {"title": "Introduction"}]
    section_entries = [{"title": "Overview"}, {"title": "Introduction"}]

    # Use a temporary file
    with tempfile.NamedTemporaryFile(suffix=".xlsx", delete=False) as tmp_file:
        output_path = tmp_file.name

    try:
        # Generate report
        Validator.generate_report(toc_entries, section_entries, output_path)

        # Check that the file was created
        assert os.path.exists(output_path), "Excel report file should be created"

        # Check the content using pandas
        df = pd.read_excel(output_path)
        assert "check" in df.columns, "Excel should have 'check' column"
        assert "toc_count" in df.columns, "Excel should have 'toc_count' column"
        assert "parsed_count" in df.columns, "Excel should have 'parsed_count' column"
        assert "status" in df.columns, "Excel should have 'status' column"

        # Optional: check row count
        assert len(df) == 3, "Excel report should have 3 rows (total, missing, extra)"

    finally:
        # Clean up temporary file
        if os.path.exists(output_path):
            os.remove(output_path)
