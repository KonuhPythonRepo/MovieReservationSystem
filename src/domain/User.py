from dataclasses import dataclass

@dataclass
class User:
    id : int
    first_name : str
    last_name : str
    username : str
    password_hash : str
    roles : str