from pathlib import Path
from take_note_cli.core import generic_editor_handler


class TestGenericEditorHandler:
    def test_handler_call(self, mock_subprocess: None):
        handler = generic_editor_handler.create_handler(self._config(), Path("~/tmp"))

        assert ['vi', Path('~/tmp')] == handler()

    def _config(self):
        return { "editor": "vi", "verbose": False}