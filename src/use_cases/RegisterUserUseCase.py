from domain.User import User
from database.user_repository import UserRepository
from security.hasher import Hasher

class RegisterUserUseCase:

    def __init__(self, user: UserRepository, hasher: Hasher):
        self.user = user
        self.hasher = hasher

    def execute(self, first_name: str, last_name: str, username: str, password: str) -> User:
        if self.user.get_by_name(username):
            raise ValueError("Пользователь уже существует")

        pass_hash = self.hasher.hash(password)

        new_user = User(
            id = None,
            first_name=first_name,
            last_name=last_name,
            roles="user",
            username=username,
            password_hash=pass_hash
        )

        self.user.save_user(new_user)
        return new_user