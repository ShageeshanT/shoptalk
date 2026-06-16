# Contributing to ShopTalk

Thank you for your interest in contributing!

## Development Setup

```bash
git clone https://github.com/ShageeshanT/shoptalk.git
cd shoptalk
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

## Running Tests

```bash
pytest tests/ -v
```

## Code Style

ShopTalk uses [Ruff](https://docs.astral.sh/ruff/) for linting and formatting.

```bash
ruff check src tests
ruff check --fix src tests
```

## Commit Message Convention

We use [Conventional Commits](https://www.conventionalcommits.org/):

- `feat:` new feature
- `fix:` bug fix
- `docs:` documentation only
- `chore:` build, CI, or tooling changes
- `refactor:` code change that neither fixes a bug nor adds a feature
- `test:` adding or updating tests

## Pull Request Process

1. Fork the repo and create a feature branch
2. Write tests for new functionality
3. Ensure all tests pass and linting is clean
4. Open a PR with a clear description
5. Link any related issues
