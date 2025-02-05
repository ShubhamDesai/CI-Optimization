# parse_html_report.py
import sys
from bs4 import BeautifulSoup

def extract_failed_tests(report_path, output_path):
    with open(report_path, 'r') as f:
        soup = BeautifulSoup(f, 'html.parser')

    failed_tests = []
    for row in soup.select('tr'):
        if 'failed' in row.get('class', []):
            test_name = row.select_one('td.name').get_text()
            failed_tests.append(test_name)
    print(failed_tests)
    with open(output_path, 'w') as f:
        for test in failed_tests:
            f.write(f"{test}\n")

if __name__ == "__main__":
    report_path = sys.argv[1]
    output_path = sys.argv[2]
    extract_failed_tests(report_path, output_path)
