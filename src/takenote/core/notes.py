from datetime import date
from pathlib import Path
from takenote.utils.paths import generate_note_folder, generate_note_path


class Notes:
    def create_file(self, week: date, root_path):
        folder = generate_note_folder(week, root_path)
        print(f"folder: {folder}")

        path = folder.joinpath(generate_note_path(week))
        print(f"path: {path}")

        folder.mkdir(parents=True, exist_ok=True)
        path.touch(exist_ok=True)
