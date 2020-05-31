# Tea Shop

## Requirements

- `Python 3.8 or greater`
- `poetry`
- `yarn`

## Installation

- Clone this repo
- Optionally create virtualenv using `python -m venv .venv` and activate it using `source .venv/bin/activate`
- `cd frontend/`
- yarn install
- `yarn build`

## Start server

You can start the server with the script `run.sh` from the project directory

It will install all python dependencies using `poetry`
 ```bash
  ./run.sh
```

## Test coverge report

`poetry install` - to install dev dependencies

```bash
pytest --cov-report term-missing --cov=backend tests/

----------- coverage: platform linux, python 3.8.2-final-0 -----------
Name                  Stmts   Miss  Cover   Missing
---------------------------------------------------
backend/__init__.py       0      0   100%
backend/main.py          54      3    94%   20, 30, 35
backend/model.py          3      0   100%
backend/schema.py        12      0   100%
---------------------------------------------------
TOTAL                    69      3    96%
```
