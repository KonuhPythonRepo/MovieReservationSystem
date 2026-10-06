from database.ticket_repository import TicketRepository
from domain import Ticket


class CreateTicketUseCase:
    def __init__(self, ticket: TicketRepository):
        self.ticket = ticket

    def execute(self, seat: int, row: int, price: int, user_id: int, showtime_id: int):
        self.ticket.save_ticket(
            Ticket(
                id = None,
                seat=seat,
                row=row,
                price=price,
                user_id=user_id,
                showtime_id =  showtime_id
            )
        )

