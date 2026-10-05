import datetime

import psycopg

from src.domain.Showtime import Showtime


class ShowTimesRepository:
    def __init__(self, connection_string):
        self.connection_string = connection_string

    def get_by_id(self, id: int) -> Showtime | None:
        with psycopg.connect(self.connection_string) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM public.showtimes WHERE id = %s", (id,))
                row = cur.fetchone()
                if row is None:
                    return None
                return Showtime(
                    id=row[0],
                    movie_id=row[1],
                    hall_id=row[2],
                    start_time=row[3]
                )

    def save_showtime(self, showtime: Showtime) -> None:
        with psycopg.connect(self.connection_string) as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "INSERT INTO public.showtimes (movie_id, hall_id, start_time) VALUES (%s, %s, %s) RETURNING id",
                    (showtime.movie_id, showtime.hall_id, showtime.start_time))
                showtime.id = cur.fetchone()[0]
                conn.commit()

    def delete_showtime(self, id: int) -> None:
        with psycopg.connect(self.connection_string) as conn:
            with conn.cursor() as cur:
                cur.execute("DELETE FROM public.showtimes WHERE id = %s", (id,))
                conn.commit()

    def get_by_date(self, date: datetime.date) -> list[Showtime] | None:
        with psycopg.connect(self.connection_string) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM public.showtimes WHERE start_time::date = %s", (date,))
                rows = cur.fetchall()
                return [
                    Showtime(
                        id = show_row[0],
                        movie_id = show_row[1],
                        hall_id = show_row[2],
                        start_time = show_row[3]
                    )
                    for show_row in rows
                ]
