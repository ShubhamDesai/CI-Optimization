# test_report_generation.py

from report_generation import generate_detailed_report

def test_generate_detailed_report():
    result = generate_detailed_report()
    assert result == "Report Generation Complete"
