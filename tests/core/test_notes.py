from takenote.core.notes import Notes
from pathlib import Path
from dateutil.parser import parse


class TestNotes:
    def test_create_file(self):
        week = parse("2023-08-31")
        homepath = Path.home()
        notes = Notes()
        notes.create_file(week, homepath.joinpath("tmp/notes"))
        target_file = homepath.joinpath("tmp/notes/2023/08/2023-08-31-Weekly-log.md")
        assert target_file.exists()
