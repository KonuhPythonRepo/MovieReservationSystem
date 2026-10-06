import psycopg
from src.domain.Ticket import Ticket

class TicketRepository:
    def __init__(self, connection_string):
        self.connection_string = connection_string

    def get_by_id(self, id: int) -> Ticket | None:
        with psycopg.connect(self.connection_string) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM public.ticket WHERE id = %s", (id,))
                row = cur.fetchone()
                if row is None:
                    return None
                return Ticket(
                    id = row[0],
                    seat = row[1],
                    row = row[2],
                    price = row[3],
                    user_id = row[4],
                    showtime_id = row[5]
                )

    def save_ticket(self, ticket: Ticket) -> None:
        with psycopg.connect(self.connection_string) as conn:
            with conn.cursor() as cur:
                cur.execute("INSERT INTO public.ticket (seat, row, price, user_id, showtime_id) VALUES (%s, %s, %s, %s, %s) RETURNING id", (ticket.seat, ticket.row, ticket.price, ticket.user_id, ticket.showtime_id))
                ticket.id = cur.fetchone()[0]
                conn.commit()

    def delete_ticket(self, id: int) -> None:
        with psycopg.connect(self.connection_string) as conn:
            with conn.cursor() as cur:
                cur.execute("DELETE FROM public.ticket WHERE id = %s", (id,))
                conn.commit()

    def seat_is_empty(self, ticket: Ticket) -> bool:
        with psycopg.connect(self.connection_string) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT NOT EXISTS( SELECT 1 FROM public.ticket WHERE seat = %s AND row = %s AND showtime_id = %s)",(ticket.seat, ticket.row, ticket.showtime_id))
                row = cur.fetchone()
                return row[0]

    def all_tickets(self, showtime_id: int) -> list[Ticket]:
        with psycopg.connect(self.connection_string) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM public.ticket WHERE showtime_id = %s", (showtime_id,))
                rows = cur.fetchall()
                return [
                    Ticket(
                        id = tick_row[0],
                        seat = tick_row[1],
                        row = tick_row[2],
                        price = tick_row[3],
                        user_id = tick_row[4],
                        showtime_id=tick_row[5]
                    )
                    for tick_row in rows
                ]
