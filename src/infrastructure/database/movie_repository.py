import psycopg
from domain.Movie import Movie

class MovieRepository:
    def __init__(self, connection_string):
        self.connection_string = connection_string

    def get_by_id(self, id: int) -> Movie | None:
        with psycopg.connect(self.connection_string) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM public.movie WHERE id = %s", (id,))
                row = cur.fetchone()

                if not row:
                    return None

                return Movie(
                    id = row[0],
                    name = row[1],
                    description = row[2],
                    poster_url = row[3],
                    genre = row[4],
                    duration = row[5]
                )

    def save_movie(self, movie: Movie) -> None:
        with psycopg.connect(self.connection_string) as conn:
            with conn.cursor() as cur:
                cur.execute("INSERT INTO public.movie (name, description, poster_url, genre, duration) VALUES (%s, %s, %s, %s, %s) returning id;", (movie.name, movie.description, movie.poster_url, movie.genre, movie.duration))
                movie.id = cur.fetchone()[0]
                conn.commit()

    def update_movie(self, movie: Movie) -> None:
        with psycopg.connect(self.connection_string) as conn:
            with conn.cursor() as cur:
                cur.execute("UPDATE public.movie SET name = %s, description = %s, poster_url = %s, genre = %s, duration = %s where id = %s",(movie.name, movie.description, movie.poster_url, movie.genre, movie.duration, movie.id))
                conn.commit()

    def delete_movie(self, id: int) -> None:
        with psycopg.connect(self.connection_string) as conn:
            with conn.cursor() as cur:
                cur.execute("DELETE FROM public.movie WHERE id = %s", (id,))
                conn.commit()

    def get_all_movies(self) -> list[Movie]:
        with psycopg.connect(self.connection_string) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM public.movie")
                rows = cur.fetchall()
                return [
                    Movie(
                        id = mov_row[0],
                        name = mov_row[1],
                        description = mov_row[2],
                        poster_url = mov_row[3],
                        genre = mov_row[4],
                        duration = mov_row[5]
                    )
                    for mov_row in rows
                ]