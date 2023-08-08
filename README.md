# Take Note
**Create and open notes in your favourite editor.**

## Features

- Open notes files for this week, last week or next week from the cli in your favourite editor
- Organises notes in a date based folder structure from your root notes folder, e.g. 2023/08
- When the file doesn't already exist, it uses an optional template to create the file. A sample template is supplied.

## Future features

- Support for daily notes options.

## Installation


## Usage



## Development

### Nix & NixOS

The supplied shell.nix definition provides support for entering a nix-shell directly in the repository with all dependencies.

````
nix-shell

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
