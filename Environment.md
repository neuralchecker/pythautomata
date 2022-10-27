# Environment

## Python (>= 3.9v && < 3.11v)

- Debian, Ubuntu and derivatives: `apt install python3.9`
- Rhel and Fedora: `dnf install python3`
- Arch and Manjaro: `pacman -Sy python3`
- MacOS and Linux with *homebrew* installed: `brew install python`
- Windows: visit https://www.python.org/downloads/

## Pip
- *nix: `curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py`
- `python3 get-pip.py`
- Windows: `python get-pip.py`


## Poetry

- *nix: `curl -sSL https://install.python-poetry.org | python3 -`
- `poetry config virtualenvs.in-project true`
- Windows (Powershell): `(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -`

### Adding poetry to $PATH

#### *nix

- `code ~/.bashrc` [bash]
- `code ~/.zshrc` [zsh]
- At the end of the file add: `export PATH=$/home/username/ local/bin:$PATH`

#### Windows

- Search Edit the system environment variables
- Environment variables...
- Click Edit in Path in System variables section
- New
- Add given path
- Save

### Installing dependencies

- `poetry install`

## Pythautomata

- `pip install pythautomata`

## Run Tests

```
poetry run python pythautomata/run_tests.py
```




