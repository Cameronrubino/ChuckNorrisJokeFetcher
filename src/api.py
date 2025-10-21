"""API client for ChuckNorrisJokeFetcher."""

BASE = "https://api.chucknorris.io/jokes"

try:
    import requests
except Exception:
    requests = None


def _get(path, params=None):
    if requests is None:
        raise RuntimeError("requests required")
    r = requests.get(f"{BASE}/{path}", params=params, timeout=5.0)
    r.raise_for_status()
    return r.json()


def fetch_random_joke():
    return _get("random")


def list_categories():
    return _get("categories")


def search_jokes(query):
    if not query:
        return {"total": 0, "result": []}
    return _get("search", params={"query": query})
