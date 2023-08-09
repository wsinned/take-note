import pytest
from datetime import date
from dateutil.parser import parse
from takenote.utils.dates import get_monday, format_header_date, format_file_date

class TestDates:

    def test_get_monday(self):
        tuesday = parse("2023-08-08")
        monday = get_monday(tuesday)
        assert monday.day == 7
    
    def test_last_month_get_monday(self):
        tuesday = parse("2023-08-01")
        monday = get_monday(tuesday)
        assert monday.day == 31
        assert monday.month == 7

    def test_last_year_get_monday(self):
        wednesday = parse("2025-01-01")
        monday = get_monday(wednesday)
        assert monday.day == 30
        assert monday.month == 12
        assert monday.year == 2024 

    def test_today_is_monday_get_monday(self):
        today = parse("2023-08-07")
        monday = get_monday(today)
        assert monday == today

    def test_header_date(self):
        day = parse("2023-08-08")
        assert format_header_date(day) == "Tuesday 08 August 2023"

    def test_file_date(self):
        day = parse("2023-08-31")
        assert format_file_date(day) == "2023-08-31"