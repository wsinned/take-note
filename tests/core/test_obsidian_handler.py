from take_note_cli.core import obsidian_handler


class TestObsidianHandler:
    def test_handler_call(self, mock_subprocess: None):
        handler = obsidian_handler.create_handler(self._config(), "~/tmp/MyFile.md")

        assert ["start", "obsidian://open?path=~/tmp/MyFile.md"] == handler()

    def _config(self):
        return {"editor": "obsidian", "verbose": False}
