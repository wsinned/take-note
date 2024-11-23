from pathlib import Path
from take_note_cli.core import vscode_handler


class TestVSCodeHandler:
    def test_handler_call(self, mock_subprocess: None):
        handler = vscode_handler.create_handler(self._config(), Path("~/tmp"))

        assert ['code', Path('~/tmp'), Path("~/tmp/my.code-workspace")] == handler()

    def _config(self):
        return { "editor": "code", "notesFolder": Path("~/tmp"), "workspace": "my.code-workspace", "verbose": False}
