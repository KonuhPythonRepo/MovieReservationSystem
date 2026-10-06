from database.user_repository import UserRepository
from security.hasher import Hasher

class LoginUserUseCase:

    def __init__(self, user_repo: UserRepository, hash: Hasher):
        self.user_repo = user_repo
        self.hash = hash

    def login(self, username: str, password: str):
        user = self.user_repo.get_by_name(username)

        if not user:
            raise ValueError("User not found")

        if not self.hash.verify(password, user.password_hash):
            raise ValueError("Invalid password")

        print(f"Успешная авторизация пользователя {user.username}")
        return user

