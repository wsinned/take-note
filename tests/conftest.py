import pytest


@pytest.fixture(autouse=True)
def mock_subprocess(monkeypatch):
    def mock_subprocess_call(_):
        print("FAKING CALL")
        return "FAKE"

    monkeypatch.setattr("takenote.core.notes.call", mock_subprocess_call)
