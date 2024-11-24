import pytest


@pytest.fixture(autouse=True)
def mock_subprocess(monkeypatch):
    def mock_subprocess_call(args):
        print("FAKING CALL")
        return args

    monkeypatch.setattr(
        "take_note_cli.core.generic_editor_handler.call", mock_subprocess_call
    )
    monkeypatch.setattr("take_note_cli.core.vscode_handler.call", mock_subprocess_call)
    monkeypatch.setattr(
        "take_note_cli.core.obsidian_handler.call", mock_subprocess_call
    )


@pytest.fixture(autouse=True)
def mock_platform(monkeypatch):
    def mock_platform_call():
        return "darwin"

    monkeypatch.setattr(
        "take_note_cli.core.obsidian_handler.sys.platform", mock_platform_call
    )
