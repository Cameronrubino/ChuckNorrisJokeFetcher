import io
import sys
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src import main


def capture(argv):
    old = sys.stdout
    sys.stdout = io.StringIO()
    try:
        try:
            rc = main.main(argv)
        except SystemExit as se:
            # argparse may call sys.exit when `--help` is used; capture it as rc
            rc = se.code if isinstance(se.code, int) else 0
        return rc, sys.stdout.getvalue()
    finally:
        sys.stdout = old


def test_help():
    rc, out = capture(["--help"])
    assert rc in (0, 2)
    assert "Chuck Norris jokes CLI" in out
