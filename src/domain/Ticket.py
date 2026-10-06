from dataclasses import dataclass
from datetime import date


@dataclass
class Ticket:
    id: int | None
    seat: int
    row: int
    price: int
    user_id: int
    showtime_id: int