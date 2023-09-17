from takenote.utils import args
from pathlib import Path

class TestArgs:
    def test_parse_notes_folder(self):
        options = args.process_args(['--notesFolder', '/tmp/notes'])
        assert options.notesFolder == Path('/tmp/notes')

    def test_default_notes_folder(self):
        options = args.process_args([])
        assert options.notesFolder == Path.home().joinpath("Notes")

