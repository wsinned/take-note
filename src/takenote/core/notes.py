from datetime import date
from takenote.utils.paths import generate_note_folder, generate_note_path
from takenote.utils.dates import get_monday, get_time_delta_from_options
from takenote.utils.args import process_args
from subprocess import call


def create_file(week: date, folder_path):
    folder = generate_note_folder(week, folder_path)
    print(f"folder: {folder}")

    path = folder.joinpath(generate_note_path(week))

    folder.mkdir(parents=True, exist_ok=True)
    path.touch(exist_ok=True)
    return path


def open_file(week: date, folder_path):
    note_file = create_file(week, folder_path)
    call(["code", note_file])
    return note_file


def main(argv):
    options = process_args(argv)
    delta = get_time_delta_from_options(options)
    monday = get_monday(date.today()) + delta
    open_file(monday, options.notesFolder)
