import psycopg
from src.domain.Movie import Movie

class MovieRepository:
    def __init__(self, connection_string):
        self.connection_string = connection_string

    def get_by_id(self, id: int) -> Movie | None:
        with psycopg.connect(self.connection_string) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM public.movies WHERE id = %s", (id,))
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
                cur.execute("INSERT INTO public.movies (name, description, poster_url, genre, duration) VALUES (%s, %s, %s, %s, %s) returning id;", (movie.name, movie.description, movie.poster_url, movie.genre, movie.duration))
                movie.id = cur.fetchone()[0]
                conn.commit()
