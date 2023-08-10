from takenote.utils import args
from pathlib import Path

class TestArgs:
    def test_parse_notes_folder(self):
        notes_folder = args.process_args(['--notesFolder', '/tmp/notes'])
        assert notes_folder == Path('/tmp/notes')

    def test_default_notes_folder(self):
        notes_folder = args.process_args([])
        assert notes_folder == Path.home().joinpath("Notes")