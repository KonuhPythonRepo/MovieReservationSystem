from dataclasses import dataclass

@dataclass
class Movie:
    id: int | None
    name: str
    description: str
    poster_url: str
    genre: str
    duration: int