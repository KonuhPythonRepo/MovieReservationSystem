import datetime

from database.showtime_repository import ShowTimesRepository
from domain import Showtime


class CreateShowtimeUseCase:

    def __init__(self, showtime: ShowTimesRepository):
        self.showtime = showtime

    def execute(self, movie_id: int, hall_id: int, start_time: datetime.datetime):
        self.showtime.save_showtime(
            Showtime(
                id = None,
                movie_id=movie_id,
                hall_id=hall_id,
                start_time=start_time
            )
        )