from pathlib import Path
from datetime import date
from takenote.utils.dates import format_file_date


def generate_note_path(week: date):
    return Path(f"{format_file_date(week)}-Weekly-log.md")


def generate_note_folder(week: date, path):
    return Path.joinpath(path, week.strftime("%Y"), week.strftime("%m"))
