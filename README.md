# Python UV Project Template

This repository provides a modern, high-performance template for Python projects using [uv](https://github.com/astral-sh/uv), an extremely fast Python package manager and environment tool.

## Features

- **Fast Dependency Management:** Powered by `uv` for near-instant installation.
- **Modern Linting & Formatting:** Integrated with [Ruff](https://github.com/astral-sh/ruff) for lightning-fast code quality checks.
- **Testing Suite:** Pre-configured with [pytest](https://docs.pytest.org).
- **Strict Code Standards:** Includes `.editorconfig` and `.gitattributes` to ensure consistent formatting (LF line endings, UTF-8, 4-space indentation) across all OS and editors.
- **Robust CI/CD:** GitHub Actions workflow that validates formatting, linting, and runs tests on every push to any branch.

## Quick Start

```bash
# Clone the template
git clone https://github.com/Evr5/python-uv-template.git my-new-project
cd my-new-project

# Initialize and run
uv sync
uv run src/main.py
```

## Requirements

This project requires:

- **Python 3.12 or later**
- [uv](https://github.com/astral-sh/uv) installed on your system

## Installation

Clone the repository and install dependencies:

```bash
uv sync
```

This command creates a virtual environment in `.venv`  and installs all dependencies and dev tools defined in `pyproject.toml`

## Usage

### Running the Project

```bash
uv run src/main.py
```

### Running Tests

```bash
uv run pytest
```

### Formatting and Linting

Check for errors and formatting issues:

```bash
uv run ruff check .
uv run ruff format . --check
```

Automatically fix linting errors and format code:

```bash
uv run ruff check . --fix
uv run ruff format .
```

### Type Checking

To check types with mypy:

```bash
uv run mypy .
```

## Managing Dependencies

Add a production dependency:

```bash
uv add requests
```

Add a development dependency:

```bash
uv add --dev mypy
```

## Project Structure

```bash
project-root/
├── .github/workflows/ci.yml  # Multi-stage CI (Lint -> Test)
├── src/
│   └── main.py               # Entry point
├── tests/
│   ├── conftest.py           # Pytest configuration
│   └── test_main.py          # Example tests
├── .editorconfig             # Editor consistency rules
├── .gitattributes            # Git line ending management (LF)
├── .gitignore                # Python & uv specific ignores
├── .python-version           # Target Python version (3.12+)
├── pyproject.toml            # Project & tool configuration
├── uv.lock                   # Deterministic lockfile (versioned)
└── README.md
```

## IDE Support

To get the most out of this template, we recommend:

- **VS Code:** Install the `EditorConfig` extension to automatically apply the rules defined in .editorconfig.
- **PyCharm:** Support is built-in.
- **Neovim:** Support is built-in (since version 0.9). For older versions, the editorconfig-vim plugin is required.

## Continuous Integration

The included GitHub Actions workflow (`.github/workflows/ci.yml`) automatically runs on every `push` and `pull_request` for all branches. It performs:

- **Lint & Format Check:** Uses Ruff to ensure code quality.
- **Test Suite:** Runs Pytest across the environment.

## License

This project is licensed under the **MIT License**.
See the [LICENSE](./LICENSE) file for details.
