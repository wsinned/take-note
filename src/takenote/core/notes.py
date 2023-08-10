from datetime import date
from takenote.utils.paths import generate_note_folder, generate_note_path
from takenote.utils.dates import get_monday
from takenote.utils.args import process_args


def create_file(week: date, root_path):
    folder = generate_note_folder(week, root_path)
    print(f"folder: {folder}")

    path = folder.joinpath(generate_note_path(week))


    folder.mkdir(parents=True, exist_ok=True)
    path.touch(exist_ok=True)


def main(argv):
    notes_folder = process_args(argv)
    monday = get_monday(date.today())
    create_file(monday, notes_folder)
