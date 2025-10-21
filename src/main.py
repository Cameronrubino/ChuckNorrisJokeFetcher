"""CLI entrypoint for ChuckNorrisJokeFetcher."""

from __future__ import annotations

import argparse
import sys
from . import api


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="chuck", description="Chuck Norris jokes CLI")
    sub = parser.add_subparsers(dest="command")

    p = sub.add_parser("random", help="Random joke")
    p.set_defaults(func=lambda args: print(api.fetch_random_joke().get("value")) or 0)

    p = sub.add_parser("categories", help="List categories")
    p.set_defaults(func=lambda args: [print(c) for c in api.list_categories()] or 0)

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

    return parser


def main(argv: list[str] | None = None) -> int:
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
