import bcrypt

class Hasher:
    def hash(self, password: str) -> str:
        salt = bcrypt.gensalt(12)
        result = bcrypt.hashpw(password.encode("utf-8"), salt)
        return result.decode("utf-8")

    def verify(self, password: str, hash: str) -> bool:
        return bcrypt.checkpw(password.encode("utf-8"), hash.encode("utf-8"))