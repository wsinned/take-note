import pytest
from datetime import date
from dateutil.parser import parse
from takenote.utils.dates import get_monday

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
