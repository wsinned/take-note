from takenote.core import notes
from pathlib import Path
from dateutil.parser import parse


class TestNotes:
    def test_create_file(self):
        week = parse("2023-08-31")
        homepath = Path.home()
        note_file = notes.create_file(week, homepath.joinpath("tmp/notes"))
        target_file = homepath.joinpath("tmp/notes/2023/08/2023-08-31-Weekly-log.md")
        assert target_file.exists()
        assert target_file == note_file

    def test_open_file(self, mock_subprocess):
        week = parse("2023-08-31")
        homepath = Path.home()
        note_file = notes.open_file(week, homepath.joinpath("tmp/notes"))
        target_file = homepath.joinpath("tmp/notes/2023/08/2023-08-31-Weekly-log.md")
        note_file = notes.open_file(week, homepath.joinpath("tmp/notes"))
        assert note_file == target_file

    def test_entry_point(self):
        notes.main([])
