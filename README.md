# Take Note
**Create and open notes in your favourite editor.**

## Features

- Open notes files for this week using the `code` command line for VS Code.
- Organises notes in a date based folder structure from your root notes folder, e.g. 2023/08
    - set the root notes folder using --notesFolder

## Future features
- Support for choosing the editor used.
- Open the file for last week or next week.
- When the file doesn't already exist, it uses an optional template to create the file. A sample template is supplied.
- Support for daily notes options.


## Installation

Presently only running installed in the virtual environment is supported.

```
python -m venv venv 

source venv/bin/activate

# install with tests as editable src
venv/bin/pip3 install .

venv/bin/take-note --notesFolder=$HOME/MyNotes
```

## Usage

Spefify a folder using the --notesFolder option, otherwise $HOME/Notes will be used

```
venv/bin/take-note --notesFolder=$HOME/MyNotes
```

A note will be created in the under the MyNotes/YYYY/mm folder named with the date of the Monday of this week, e.g. 2023-08-07-Weekly-log.md



## Development

### Nix & NixOS

The supplied shell.nix definition provides support for entering a nix-shell directly in the repository with all dependencies.

````
nix-shell --run zsh # ensure using zsh over default bash session

# only needed once, or to recreate the virtual environment
python -m venv venv 

source venv/bin/activate

# install with tests as editable src
venv/bin/pip3 install -e '.[test]'

# run the tests
pytest

# close the virtual environment and exit the shell when done
deactivate
exit
````


### Other Linux or MacOS

````
# only needed once, or to recreate the virtual environment
python -m venv venv 

source venv/bin/activate

venv/bin/pip3 install -r requirements.txt -r requirements.dev.txt

# install with tests as editable src
venv/bin/pip3 install -e '.[test]'

# run the tests
venv/bin/pytest

# close the virtual environment when done
deactivate
````
