from datetime import datetime
from datetime_utils import format_date

def test_format_date():
    date = datetime(2025, 2, 14)
    assert format_date(date, "%Y-%m-%d") == "2025-02-14"