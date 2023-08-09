import pytest
from datetime import date
from dateutil.parser import parse
from pathlib import Path
from takenote.utils.paths import generate_note_path

class TestPaths:

    def test_note_path(self):
        week = parse("2023-08-31")
        target_path = Path("/tmp/2023-08-31-Weekly-log.md")
        assert generate_note_path(week, Path("/tmp")) == target_path
