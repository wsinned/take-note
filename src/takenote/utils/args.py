import argparse
import pathlib
from sys import exit


def init_argparse() -> argparse.ArgumentParser:
    help_text = """Create a notes file for the requested 
        week."""

    parser = argparse.ArgumentParser(usage="%(prog)s [OPTIONS]", description=help_text)
    parser.add_argument(
        "-v", "--version", action="version", version=f"{parser.prog} version 0.0.1"
    )
    parser.add_argument(
        "--notesFolder",
        default=pathlib.Path.home().joinpath("Notes"),
        type=pathlib.Path,
        help="""The root path for the notes folder. 
        If not supplied this defaults to the Notes folder in the users home folder."""
    )

    return parser


def process_args(args):
    parser = init_argparse()
    parsed = parser.parse_args(args)

    return parsed
