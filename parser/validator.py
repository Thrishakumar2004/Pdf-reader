import pandas as pd

class Validator:
    @staticmethod
    def generate_report(toc_entries, parsed_entries, output_path):
        toc_count = len(toc_entries)
        parsed_count = len(parsed_entries)

        missing_in_parsed = max(toc_count - parsed_count, 0)
        extra_in_parsed = max(parsed_count - toc_count, 0)

        # Determine status for total sections
        total_status = "PASS" if toc_count == parsed_count else "FAIL"

        data = [
            {"check": "Total sections", "toc_count": toc_count, "parsed_count": parsed_count, "status": total_status},
            {"check": "Missing in parsed", "toc_count": missing_in_parsed, "parsed_count": missing_in_parsed, "status": "OK"},
            {"check": "Extra in parsed", "toc_count": extra_in_parsed, "parsed_count": extra_in_parsed, "status": "OK"},
        ]

        df = pd.DataFrame(data)
        df.to_excel(output_path, index=False)
        print(f"Validation report saved to {output_path}")
