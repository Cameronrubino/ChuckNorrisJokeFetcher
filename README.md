# ChuckNorrisJokeFetcher

[![Tests](https://github.com/Cameronrubino/ChuckNorrisJokeFetcher/actions/workflows/tests.yml/badge.svg)](https://github.com/Cameronrubino/ChuckNorrisJokeFetcher/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)

Small CLI to fetch Chuck Norris jokes.

## Features

- Fetch a random Chuck Norris joke
- List available joke categories
- Search jokes by query

## Installation

1. Clone the repo:

	git clone <repo-url>
	cd ChuckNorrisJokeFetcher

2. Create and activate a virtual environment (Python 3.10+):

	python -m venv .venv
	.\.venv\Scripts\Activate.ps1  # PowerShell on Windows

3. Install dependencies:

	pip install -r requirements.txt

## Usage

You can run the CLI directly from the package module:

	python -m src --help

Examples:

	python -m src random
	python -m src categories
	python -m src search karate

The project also supports running the main module directly:

	python -m src.main --help

## API Information

This project uses the free public Chuck Norris API:

- Base URL: https://api.chucknorris.io/jokes
- Endpoints used: `/random`, `/categories`, `/search`

API docs: https://api.chucknorris.io/

## Testing

Run the test suite locally:

	pytest tests/

Tests mock `requests` in `tests/test_api.py` so they run offline.

## Technologies

- Python 3.10+
- requests
- pytest

## Badges

Add repository and CI badges here (Actions, license) as desired.

---

Verification steps (for Canvas):

1. Clone the repo.
2. Create venv and install requirements.
3. Run `pytest tests/`.
4. Run `python -m src --help`.
