"""API client for ChuckNorrisJokeFetcher.

This module wraps the external Chuck Norris API. Functions will raise
RuntimeError when the `requests` dependency is not available. Unit tests
should monkeypatch `api.requests` to a dummy object to avoid network calls.
"""

BASE = "https://api.chucknorris.io/jokes"

try:
    import requests
except Exception:
    requests = None


def _get(path, params=None):
    """Perform a GET request to the given path on the API and return parsed JSON.

    Args:
        path (str): path under the BASE URL (e.g. 'random' or 'search')
        params (dict|None): optional query parameters

    Raises:
        RuntimeError: if `requests` is not installed.
        requests.HTTPError: when the remote returns a non-2xx status.
    """
    if requests is None:
        raise RuntimeError("requests required")
    r = requests.get(f"{BASE}/{path}", params=params, timeout=5.0)
    r.raise_for_status()
    return r.json()


def fetch_random_joke():
    """Return a single random joke as a dict.

    Example return: {"categories": [], "created_at": "...", "value": "..."}
    """
    return _get("random")


def list_categories():
    """Return a list of available joke categories.

    Example return: ["animal", "dev"]
    """
    return _get("categories")


def search_jokes(query):
    """Search jokes by query string.

    Args:
        query (str): search query; if falsy, returns an empty result structure.

    Returns:
        dict: a structure containing `total` and `result` keys when query is
              provided; otherwise returns `{"total": 0, "result": []}`.
    """
    if not query:
        return {"total": 0, "result": []}
    return _get("search", params={"query": query})
