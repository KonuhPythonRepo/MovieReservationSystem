import datetime
from dataclasses import dataclass


@dataclass
class Showtime:
    id: int| None
    movie_id: int
    hall_id: int
    start_time: datetime.datetime