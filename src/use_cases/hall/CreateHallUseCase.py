from database.hall_repository import HallRepository
from domain import Hall


class CreateHallUseCase:
    def __init__(self, hall: HallRepository):
        self.hall = hall

    def execute(self, seat_count: int, is3d: bool, is_dis_person: bool,):
        self.hall.save_hall(
            Hall(
                id = None,
                seat_count = seat_count,
                is_3d=is3d,
                is_dis_person=is_dis_person,
            )
        )
