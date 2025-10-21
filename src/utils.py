"""Utility helpers for the CLI.

Small helpers that encapsulate file I/O so we can test them separately.
"""

from __future__ import annotations

import pathlib
from typing import Union


def save_quote(text: str, filename: Union[str, pathlib.Path]) -> None:
    """Append a quote to `filename`, creating directories as needed.

    Args:
        text: the quote text to save
        filename: path to the file where the quote will be appended

    Raises:
        OSError: if the file cannot be written
    """
    path = pathlib.Path(filename)
    path.parent.mkdir(parents=True, exist_ok=True)
    # Open in append mode and write the quote with a newline
    with path.open("a", encoding="utf-8") as fh:
        fh.write(text.rstrip("\n") + "\n")
