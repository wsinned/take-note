from datetime import date
from takenote.utils.paths import generate_note_folder, generate_note_path
from takenote.utils.dates import get_monday
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
    notes_folder = process_args(argv)
    monday = get_monday(date.today())
    open_file(monday, notes_folder)
