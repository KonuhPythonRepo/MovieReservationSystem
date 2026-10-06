import psycopg
from domain.Hall import Hall

class HallRepository:
    def __init__(self, connection_string):
        self.connection_string = connection_string

    def get_by_id(self, hall_id: int) -> Hall | None:
        with psycopg.connect(self.connection_string) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM public.hall WHERE id = %s", (hall_id,))
                row = cur.fetchone()
                if row is None:
                    return None
                return Hall(
                    id = row[0],
                    seat_count = row[1] ,
                    is_3d = row[2],
                    is_dis_person = row[3]
                )

    def save_hall(self, hall: Hall) -> None:
        with psycopg.connect(self.connection_string) as conn:
            with conn.cursor() as cur:
                cur.execute("INSERT INTO public.hall (seat_count, is3d, isdisperson) VALUES (%s, %s, %s) RETURNING id", ( hall.seat_count, hall.is_3d, hall.is_dis_person))
                hall.id = cur.fetchone()[0]
                conn.commit()
