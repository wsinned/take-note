from take_note_cli.utils import config
from take_note_cli.utils import args


class TestConfig:
    def test_check_config_file(self):
        cfg = config.check_for_config_file()
        assert cfg.keys()

    def test_process_config(self):
        o, _ = args.process_args(["--editor", "nvim"])
        cfg = config.process_config(o)
        assert cfg.keys()
