from pathlib import Path
from datetime import date
from takenote.utils.dates import format_file_date

def generate_note_path(week: date, path):
    return Path.joinpath(
        path, f"{format_file_date(week)}-Weekly-log.md"
    )