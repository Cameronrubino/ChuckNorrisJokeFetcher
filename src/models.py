from dataclasses import dataclass


@dataclass
class Joke:
    id: str
    value: str
    url: str | None = None
