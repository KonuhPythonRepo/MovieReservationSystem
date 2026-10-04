from dataclasses import dataclass
from datetime import date


@dataclass
class Ticket:
    id: int
    seat: int
    row: int
    price: int
    user_id: int
    movie_id: int
    hall_id: int
    demonstration_date: date