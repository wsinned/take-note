from take_note_cli.utils import args
from pathlib import Path


class TestArgs:
    def test_parse_notes_folder(self):
        options, _ = args.process_args(["--notesFolder", "/tmp/notes", "--thisWeek"])
        assert Path(options.notesFolder) == Path("/tmp/notes")

    def test_parse_notes_folder_with_space(self):
        options, _ = args.process_args(
            ["--notesFolder", "/tmp/some notes", "--thisWeek"]
        )
        assert Path(options.notesFolder) == Path("/tmp/some notes")

    def test_this_week_option_on(self):
        options, _ = args.process_args(["--thisWeek"])
        assert options.thisWeek is True

    def test_last_week_option_on(self):
        options, _ = args.process_args(["--lastWeek"])
        assert options.lastWeek is True

    def test_next_week_option_on(self):
        options, _ = args.process_args(["--nextWeek"])
        assert options.nextWeek is True

    def test_this_week_options_not_supplied(self):
        options, _ = args.process_args([])
        assert options.thisWeek is False
        assert options.lastWeek is False
        assert options.nextWeek is False

    def test_editor_option(self):
        options, _ = args.process_args(["--editor", "nvim", "--thisWeek"])
        assert options.editor == "nvim"

    def test_workspace_option(self):
        options, _ = args.process_args(
            ["--workspace", "notes.code-workspace", "--thisWeek"]
        )
        print(options)
        assert options.workspace == "notes.code-workspace"

    def test_template_option(self):
        options, _ = args.process_args(["--lastWeek", "--template", "a-template.md"])
        assert options.template == "a-template.md"

    def test_batch_option(self):
        options, _ = args.process_args(["--thisWeek", "--batch", "2"])
        assert options.batch == 2
