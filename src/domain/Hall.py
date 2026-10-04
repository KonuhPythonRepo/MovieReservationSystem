from dataclasses import dataclass

@dataclass
class Hall:
    id: int
    seat_count: int
    is_3d: bool
    is_dis_person: bool