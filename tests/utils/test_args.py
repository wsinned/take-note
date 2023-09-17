from takenote.utils import args
from pathlib import Path


class TestArgs:
    def test_parse_notes_folder(self):
        options = args.process_args(["--notesFolder", "/tmp/notes", "--thisWeek"])
        assert options.notesFolder == Path("/tmp/notes")

    def test_default_notes_folder(self):
        options = args.process_args(["--thisWeek"])
        assert options.notesFolder == Path.home().joinpath("Notes")

    def test_this_week_option_on(self):
        options = args.process_args(["--thisWeek"])
        assert options.thisWeek == True

    def test_this_week_option_off(self):
        options = args.process_args([])
        assert options.thisWeek == False
