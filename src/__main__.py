"""Make the package runnable as a module: python -m src

This forwards execution to src.main.main so `--help` and other args work
when running `python -m src`.
"""

from .main import main


def _run():
    raise SystemExit(main())


if __name__ == "__main__":
    _run()
