"""CLI entrypoint for ChuckNorrisJokeFetcher.

This module exposes a small argparse-based CLI with subcommands:

- random: print a single random joke
- categories: list available joke categories
- search: search jokes by query

Functions:
    build_parser() -> argparse.ArgumentParser: Construct the CLI parser.
    main(argv: list[str] | None = None) -> int: CLI entrypoint used by tests and
        when running the package as a module.
"""

from __future__ import annotations

import argparse
import sys
from . import api


def build_parser() -> argparse.ArgumentParser:
    """Build and return the top-level argument parser.

    Returns an argparse.ArgumentParser configured with subcommands and
    `func` defaults so `main` can dispatch. This is separated so tests can
    construct the parser without invoking network calls.
    """
    parser = argparse.ArgumentParser(prog="chuck", description="Chuck Norris jokes CLI")
    sub = parser.add_subparsers(dest="command")

    p = sub.add_parser("random", help="Random joke")
    p.set_defaults(func=lambda args: print(api.fetch_random_joke().get("value")) or 0)

    p = sub.add_parser("categories", help="List categories")
    def _list_categories(args):
        for c in api.list_categories():
            print(c)
        return 0
    p.set_defaults(func=_list_categories)

    p = sub.add_parser("search", help="Search jokes")
    p.add_argument("query")
    def _search(args):
        res = api.search_jokes(args.query)
        total = res.get("total") if isinstance(res, dict) else None
        items = res.get("result") if isinstance(res, dict) else res
        if total is not None:
            print(f"Found {total} jokes")
        if not items:
            print("No jokes found.")
            return 0
        for it in items:
            print(it.get("value"))
        return 0
    p.set_defaults(func=_search)

    p = sub.add_parser("save", help="Save a random joke to a file")
    p.add_argument("filename", help="File to append the joke to")
    def _save(args):
        from . import utils

        joke = api.fetch_random_joke().get("value")
        try:
            utils.save_quote(joke, args.filename)
            print(f"Saved quote to {args.filename}")
            return 0
        except Exception as exc:
            print(f"Error saving quote: {exc}")
            return 1

    p.set_defaults(func=_save)

    return parser


def main(argv: list[str] | None = None) -> int:
    """Run the CLI with the provided argv list (or sys.argv by default).

    Returns an int exit code. This function is safe to call from tests.
    It catches exceptions and returns non-zero on error.
    """
    argv = argv if argv is not None else sys.argv[1:]
    parser = build_parser()
    args = parser.parse_args(argv)
    if not hasattr(args, "func"):
        parser.print_help()
        return 2
    try:
        return args.func(args)
    except Exception as exc:
        print(f"Error: {exc}")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
