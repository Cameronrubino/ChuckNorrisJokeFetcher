import io
import sys

from src import main


def capture(argv):
    old = sys.stdout
    sys.stdout = io.StringIO()
    try:
        try:
            rc = main.main(argv)
        except SystemExit as se:
            rc = se.code if isinstance(se.code, int) else 0
        return rc, sys.stdout.getvalue()
    finally:
        sys.stdout = old


def test_random_command(monkeypatch):
    monkeypatch.setattr(
        "src.api.fetch_random_joke", lambda: {"value": "hi there"}
    )
    rc, out = capture(["random"])
    assert rc == 0
    assert "hi there" in out


def test_categories_command(monkeypatch):
    monkeypatch.setattr("src.api.list_categories", lambda: ["a", "b"])
    rc, out = capture(["categories"])
    assert rc == 0
    # Ensure categories printed and no stray list/None output
    assert "a" in out and "b" in out
    assert "None" not in out
    assert "[" not in out and "]" not in out


def test_save_command(monkeypatch, tmp_path):
    # Mock API to return a known joke
    monkeypatch.setattr(
        "src.api.fetch_random_joke", lambda: {"value": "saved quote"}
    )
    fname = tmp_path / "quotes.txt"
    rc, out = capture(["save", str(fname)])
    assert rc == 0
    assert "Saved quote to" in out
    # file contains the saved quote
    text = fname.read_text(encoding="utf-8")
    assert "saved quote" in text
import io
import sys

from src import main


def capture(argv):
    old = sys.stdout
    sys.stdout = io.StringIO()
    try:
        try:
            rc = main.main(argv)
        except SystemExit as se:
            rc = se.code if isinstance(se.code, int) else 0
        return rc, sys.stdout.getvalue()
    finally:
        sys.stdout = old


def test_random_command(monkeypatch):
    monkeypatch.setattr(
        "src.api.fetch_random_joke", lambda: {"value": "hi there"}
    )
    rc, out = capture(["random"])
    assert rc == 0
    assert "hi there" in out


def test_categories_command(monkeypatch):
    monkeypatch.setattr("src.api.list_categories", lambda: ["a", "b"])
    rc, out = capture(["categories"])
    assert rc == 0
    assert "a" in out and "b" in out


def test_save_command(monkeypatch, tmp_path):
    # Mock API to return a known joke
    monkeypatch.setattr(
        "src.api.fetch_random_joke", lambda: {"value": "saved quote"}
    )
    fname = tmp_path / "quotes.txt"
    rc, out = capture(["save", str(fname)])
    assert rc == 0
    assert "Saved quote to" in out
    # file contains the saved quote
    text = fname.read_text(encoding="utf-8")
    assert "saved quote" in text
import io
import sys

from src import main


def capture(argv):
    old = sys.stdout
    sys.stdout = io.StringIO()
    try:
        try:
            rc = main.main(argv)
        except SystemExit as se:
            rc = se.code if isinstance(se.code, int) else 0
        return rc, sys.stdout.getvalue()
    finally:
        sys.stdout = old


def test_random_command(monkeypatch):
    # monkeypatch the API to return a known joke
    monkeypatch.setattr(
        "src.api.fetch_random_joke", lambda: {"value": "hi there"}
    )
    rc, out = capture(["random"])
    assert rc == 0
    assert "hi there" in out


def test_categories_command(monkeypatch):
    monkeypatch.setattr("src.api.list_categories", lambda: ["a", "b"])
    rc, out = capture(["categories"])
    assert rc == 0
    assert "a" in out and "b" in out
