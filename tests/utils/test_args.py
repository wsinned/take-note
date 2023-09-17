from takenote.utils import args
from pathlib import Path


class TestArgs:
    def test_parse_notes_folder(self):
        options, _ = args.process_args(["--notesFolder", "/tmp/notes", "--thisWeek"])
        assert options.notesFolder == Path("/tmp/notes")

    def test_default_notes_folder(self):
        options, _ = args.process_args(["--thisWeek"])
        assert options.notesFolder == Path.home().joinpath("Notes")

    def test_this_week_option_on(self):
        options, _ = args.process_args(["--thisWeek"])
        assert options.thisWeek == True

    def test_last_week_option_on(self):
        options, _ = args.process_args(["--lastWeek"])
        assert options.lastWeek == True

    def test_next_week_option_on(self):
        options, _ = args.process_args(["--nextWeek"])
        assert options.nextWeek == True

    def test_this_week_options_not_supplied(self):
        options, _ = args.process_args([])
        assert options.thisWeek == False
        assert options.lastWeek == False
        assert options.nextWeek == False

    def test_editor_option(self):
        options, _ = args.process_args(["--editor", "nvim", "--thisWeek"])
        assert options.editor == "nvim"
