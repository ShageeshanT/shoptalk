# Contributing to ShopTalk

Thank you for your interest in contributing to ShopTalk! This guide covers everything you need to get started.

## Table of Contents

- [Development Setup](#development-setup)
- [Project Structure](#project-structure)
- [Making Changes](#making-changes)
- [Pull Request Process](#pull-request-process)
- [Code Style](#code-style)
- [Testing](#testing)
- [Commit Messages](#commit-messages)

---

## Development Setup

### Prerequisites

- Python 3.11 or higher
- Git

### Steps

```bash
# 1. Fork and clone the repository
git clone https://github.com/YOUR_USERNAME/shoptalk.git
cd shoptalk

# 2. Create a virtual environment
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# 3. Install in editable mode with dev dependencies
pip install -e ".[dev]"

# 4. Set up environment variables
cp .env.example .env
# Edit .env with your API keys

# 5. Run the test suite to confirm everything works
pytest

# 6. Start the development server
uvicorn shoptalk.main:app --reload
```

---

## Project Structure

```
shoptalk/
├── src/
│   └── shoptalk/          # Main application package
│       ├── adapters/      # Channel adapters (WhatsApp, Telegram, etc.)
│       ├── main.py        # FastAPI app entry point
│       ├── schemas.py     # Pydantic request/response models
│       ├── storage.py     # In-memory repository
│       └── analyzer.py    # Message analysis logic
├── tests/                 # Test suite
├── docs/                  # Documentation
├── .github/               # GitHub Actions and templates
└── pyproject.toml         # Project metadata and dependencies
```

---

## Making Changes

1. **Create a branch** from `main`:
   ```bash
   git checkout -b feat/your-feature-name
   ```

2. **Make your changes** with small, focused commits.

3. **Write or update tests** for any new functionality.

4. **Run the full test suite** before pushing:
   ```bash
   pytest
   ```

5. **Push your branch** and open a pull request.

---

## Pull Request Process

1. Fill in the pull request template completely.
2. Link any related issues using `Closes #123` in the PR description.
3. Ensure all CI checks pass.
4. Request a review from a maintainer.
5. Address review feedback promptly.
6. PRs are merged using **squash and merge** to keep history clean.

---

## Code Style

ShopTalk uses the following tools for code quality:

| Tool | Purpose |
|------|---------|
| `ruff` | Linting and formatting |
| `mypy` | Static type checking |
| `pytest` | Testing |

Run all checks:

```bash
ruff check src/ tests/
ruff format src/ tests/
mypy src/
pytest
```

### Style guidelines

- Use type hints on all function signatures.
- Write docstrings for public functions and classes.
- Keep functions small and focused on a single responsibility.
- Prefer explicit over implicit.
- Avoid abbreviations in variable names.

---

## Testing

- All new features must include tests.
- Tests live in the `tests/` directory and mirror the `src/shoptalk/` structure.
- Use `pytest` fixtures for shared setup.
- Aim for meaningful tests over high coverage numbers.

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=shoptalk --cov-report=term-missing

# Run a specific test file
pytest tests/test_analyzer.py -v
```

---

## Commit Messages

Follow the [Conventional Commits](https://www.conventionalcommits.org/) format:

```
<type>: <short description>

[optional body]

[optional footer]
```

### Types

| Type | When to use |
|------|------------|
| `feat` | New feature |
| `fix` | Bug fix |
| `docs` | Documentation only |
| `refactor` | Code change that is not a fix or feature |
| `test` | Adding or updating tests |
| `chore` | Build process, dependency updates |
| `perf` | Performance improvement |

### Examples

```
feat: add catalog matching endpoint
fix: handle empty message text in analyzer
docs: update API_OVERVIEW with new endpoints
test: add unit tests for intent extraction
```

---

## Questions?

Open a [GitHub Discussion](https://github.com/ShageeshanT/shoptalk/discussions) or file an issue.
