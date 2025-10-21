import pathlib
import sys
import types

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src import api


class Dummy:
    def __init__(self, data, status=200):
        self._data = data
        self.status_code = status

    def raise_for_status(self):
        if not (200 <= self.status_code < 300):
            raise Exception("HTTP Error")

    def json(self):
        return self._data


def test_fetch_random(monkeypatch):
    monkeypatch.setattr(api, "requests", types.SimpleNamespace(get=lambda *a, **k: Dummy({"value":"x"})))
    assert api.fetch_random_joke()["value"] == "x"


def test_list_categories(monkeypatch):
    monkeypatch.setattr(api, "requests", types.SimpleNamespace(get=lambda *a, **k: Dummy(["a","b"])))
    assert api.list_categories() == ["a","b"]


def test_search_empty():
    assert api.search_jokes("")["total"] == 0
