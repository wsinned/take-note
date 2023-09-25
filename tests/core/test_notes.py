import pytest
from takenote.core import notes
from pathlib import Path
from dateutil.parser import parse
from shutil import rmtree


class TestNotes:
    def test_create_file(self):
        week = parse("2023-08-31")
        homepath = Path.home()
        target_file = homepath.joinpath("tmp/notes/2023/08/2023-08-31-Weekly-log.md")
        assert not target_file.exists()

        note_file = notes.create_file(week, homepath.joinpath("tmp/notes"))
        assert target_file.exists()
        assert target_file == note_file

    def test_open_file_without_workspace(self, mock_subprocess):
        week = parse("2023-08-31")
        homepath = Path.home()
        target_file = homepath.joinpath("tmp/notes/2023/08/2023-08-31-Weekly-log.md")
        note_file = notes.open_file(week, homepath.joinpath("tmp/notes"), "code")
        assert note_file == target_file

    def test_open_file_with_workspace(self, mock_subprocess):
        week = parse("2023-08-31")
        homepath = Path.home()
        target_file = homepath.joinpath("tmp/notes/2023/08/2023-08-31-Weekly-log.md")
        note_file = notes.open_file(week, homepath.joinpath("tmp/notes"), "code", "some.code-workspace")
        assert note_file == target_file

    def test_entry_point(self):
        notes.main(["--thisWeek"])

    def setup_method(self):
        root = Path.home().joinpath("tmp/notes")
        if root.exists():
            rmtree(root)
            root.mkdir(parents=True)

