# Environment

## Python (>= 3.9v && < 3.11v)

- Unix: sudo apt install python3.9
- Windows: visit https://www.python.org/downloads/

## Pip
- Unix: curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py 
- python3.9 get-pip.py
- Windows: python get-pip.py

## Poetry

- Unix: curl -sSL https://install.python-poetry.org | python3 -
- Windows (Powershell): (Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -

### Adding poetry to $PATH

#### Unix

- code ~/.bashrc
- At the end of the file add: export PATH=$/home/username/.local/bin:$PATH

#### Windows

- Search Edit the system environment variables
- Environment variables...
- Click Edit in Path in System variables section
- New
- Add given path
- Save

### Installing dependencies

- poetry config virtualenvs.in-project true
- poetry install

## Pythautomata

- pip3.9 install pythautomata

## Run Tests

```
poetry run python pythautomata/run_tests.py
```




