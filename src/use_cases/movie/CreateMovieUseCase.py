from database.movie_repository import MovieRepository
from domain import Movie

class CreateMovieUseCase:
    def __init__(self, movie: MovieRepository):
        self.movie = movie

    def create(self, name: str, description: str, poster_url: str, genre: str, duration: int):
        self.movie.save_movie(Movie(
            id = None,
            name=name,
            description=description,
            poster_url=poster_url,
            genre=genre,
            duration=duration
        ))