import psycopg
from domain.User import User

class UserRepository:
    def __init__(self, connection_string):
        self.connection_string = connection_string

    def get_by_id(self, id: int) -> User | None:
        with psycopg.connect(self.connection_string) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM public.users WHERE id = %s", (id,))
                row = cur.fetchone()
                if row is None:
                    return None
                return User(
                    id = row[0],
                    first_name= row[1],
                    last_name= row[2],
                    roles = row[3],
                    username = row[4],
                    password_hash= row[5]
            )

    def get_by_name(self, name: str):
        with psycopg.connect(self.connection_string) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM public.users WHERE username = %s", (name,))
                row = cur.fetchone()
                if row is None:
                    return None
                return User(
                    id = row[0],
                    first_name = row[1],
                    last_name = row[2],
                    roles = row[3],
                    username = row[4],
                    password_hash= row[5]
                )

    def save_user(self, user: User) -> None:
        with psycopg.connect(self.connection_string) as conn:
            with conn.cursor() as cur:
                cur.execute("INSERT INTO public.users (first_name, last_name, role, username, password_hash) VALUES (%s, %s, %s, %s, %s) RETURNING id", (user.first_name, user.last_name, user.roles, user.username, user.password_hash))
                user.id = cur.fetchone()[0]
                conn.commit()

    def update_user(self, user: User) -> None:
        with psycopg.connect(self.connection_string) as conn:
            with conn.cursor() as cur:
                cur.execute("UPDATE public.users SET first_name = %s, last_name = %s, role = %s, username = %s, password_hash = %s WHERE id = %s",(user.first_name, user.last_name, user.roles, user.username, user.password_hash, user.id))
                conn.commit()
