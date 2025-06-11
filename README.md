# GERA-Back

## Project Setup

### 1. Create Virtual Environment (Optional, if prefered you can install poetry globally on your terminal)

#### MacOS/Linux

```bash
python -m venv .venv
source .venv/bin/activate
```

#### Windows (PowerShell)

```bash
python -m venv .venv
.\.venv\Scripts\activate
```

ℹ️ For any inquiries refer to [Python: venv — Creation of virtual environments](https://docs.python.org/3/library/venv.html)

### 2. Install Poetry

Recommended installation via pipx (requires Python 3.7+):

#### 2.1. pipx installation

##### MacOS

```bash
brew install pipx
pipx ensurepath

```

##### Linux

```bash
sudo apt update
sudo apt install pipx
pipx ensurepath

```

##### Windows

Install via pip (requires pip 19.0 or later)

```bash
# If you installed python using Microsoft Store, replace `py` with `python3` in the next line.
py -m pip install --user pipx
```

ℹ️ For alternative installation methods, see the [official pipx documentation.](https://pipx.pypa.io/stable/installation/)

#### 2.2. poetry installation

##### Via pipx:

```bash
pipx install poetry
```

##### Official installer:

###### Linux, macOS, Windows (WSL)

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

###### Windows (Powershell)

```bash
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
```

ℹ️ For alternative installation methods, see the [official Poetry documentation.](https://python-poetry.org/docs/#installing-with-pipx)

### 3. Install Poetry plugin: Shell

```bash
poetry self add poetry-plugin-shell
```

#### If pipx used:

```bash
pipx inject poetry poetry-plugin-shell
```

#### If pip used:

```bash
pip install poetry-plugin-shell
```

ℹ️ For any inquiries refer to [Poetry Plugin: Shell](https://github.com/python-poetry/poetry-plugin-shell)

### 4. Install Dependencies

```bash
poetry install
```

### 5. Running the project

#### 5.1. Start the FastAPI server

```bash
poetry run uvicorn app.main:app --reload
```

or

```bash
uvicorn app.main:app --reload
```

#### 5.2. Access API

```text
http://localhost:8000

test routes:
- /test-db (for db connection test)
- health (for api testing)
```

```
.
├── app/
│   ├── __init__.py
│   ├── main.py         # FastAPI app instance
│   ├── models/         # SQLAlchemy models
│   ├── schemas/        # Pydantic models
│   ├── api/            # Route handlers
│   └── db/             # Database configuration
├── tests/              # Test files
├── alembic/            # Database migrations
├── poetry.lock         # Dependency lockfile
├── pyproject.toml      # Project configuration
└── docker-compose.yml  # Docker configuration
```

### Key Commands

| Command                | Description        |
| ---------------------- | ------------------ |
| `poetry add <package>` | Add new dependency |
| `poetry run pytest`    | Run tests          |

### Documentation

- [Uvicorn](https://www.uvicorn.org/#quickstart)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLite](https://sqlite.org/)
- [Pandas](https://pandas.pydata.org/)