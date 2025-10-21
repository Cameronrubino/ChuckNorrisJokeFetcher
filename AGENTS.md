```markdown

# AGENTS

Project assistant guidance and prompts for the ChuckNorrisJokeFetcher repository.

This file contains the prompt templates and project expectations used when
asking an AI assistant to work on this project. Use these prompts to create
small, testable, and well-documented changes.

Suggested AI prompts (user-style)

- "Create a compact CLI that fetches Chuck Norris jokes. Provide `random`, `categories`, `search`, and `save` subcommands. Keep it testable and include CI."
- "Write tests that mock network calls so CI remains deterministic. Use pytest and monkeypatch the `requests` dependency or the `src.api` module." 
- "Add a `src/__main__.py` so the package can be invoked with `python -m src` and update README usage examples accordingly."
- "Create a GitHub Actions workflow that installs the requirements and runs pytest on push and pull_request."

Project-specific notes

- API used: https://api.chucknorris.io/jokes
- Package module: `src` (entrypoint `src.main`) — run with `python -m src --help`.
- CLI subcommands implemented: `random`, `categories`, `search`, `save`.
- Tests should avoid network calls by monkeypatching `src.api` or `requests`.
- Keep changes small and well-documented; add docstrings for public functions and small unit tests for new behavior.

Desired repository structure (example)

```
your-project/
├── .github/
│   └── workflows/
│       └── tests.yml          # CI config to run tests
├── src/
│   ├── __init__.py
│   ├── __main__.py            # enables `python -m src`
│   ├── main.py                # argparse CLI
│   ├── api.py                 # API client wrapper
│   └── utils.py               # small helpers (save_quote)
├── tests/
│   ├── test_api.py
│   ├── test_main.py
│   └── test_cli.py
├── AGENTS.md                  # this file
├── README.md
├── requirements.txt
└── LICENSE
```

Quality expectations and grading tips

- Provide docstrings for all public functions and small modules.
- Add tests that cover happy-path and at least one error case per API wrapper.
- Mock external HTTP calls; tests should be deterministic and fast.
- Ensure the CLI returns appropriate exit codes (0 success, non-zero on error).
- Keep CI simple: install via `pip install -r requirements.txt` and run `pytest`.

Example small tasks for the assistant

- Add a `save` subcommand to `src/main.py` and tests verifying file contents.
- Improve README usage examples and add CI badge to README.
- Add `src/utils.py` with `save_quote` and tests that write to `tmp_path`.

Implementation notes: uses https://api.chucknorris.io

```
