import psycopg
from src.domain.Hall import Hall

class HallRepository:
    def __init__(self, connection_string):
        self.connection_string = connection_string

    def get_by_id(self, hall_id: int) -> Hall | None:
        with psycopg.connect(self.connection_string) as conn:
            cur = conn.cursor()
            cur.execute("SELECT * FROM public.halls WHERE id = %s", (hall_id,))
            row = cur.fetchone()
            if row is None:
                return None
            return Hall(
                id = row[0],
                seat_count = row[1],
                is_3d = row[2],
                is_dis_person = row[3]
            )

    def save_hall(self, hall: Hall) -> None:
        pass

