from datetime import timedelta
from dateutil.parser import parse
import pytest
from takenote.utils.dates import (
    get_monday,
    format_header_date,
    format_file_date,
    get_time_delta_from_options,
    get_weeks_delta,
)


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

    def test_get_this_week_delta_from_options(self):
        option = self._get_options()
        option.thisWeek = True
        assert get_time_delta_from_options(option) == timedelta(0)

    def test_get_next_week_delta_from_options(self):
        option = self._get_options()
        option.nextWeek = True
        assert get_time_delta_from_options(option) == timedelta(7)

    def test_get_last_week_delta_from_options(self):
        option = self._get_options()
        option.lastWeek = True
        assert get_time_delta_from_options(option) == timedelta(-7)

    def test_get_weeks_delta(self):
        assert get_weeks_delta(2) == timedelta(14)

    def test_get_negative_weeks_delta(self):
        with pytest.raises(ValueError):
            get_weeks_delta(-2)

    def _get_options(self):
        return type(
            "", (object,), {"thisWeek": False, "nextWeek": False, "lastWeek": False}
        )()
