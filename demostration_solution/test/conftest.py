from unittest.mock import MagicMock
import pytest
from demostration_solution.dao.director import DirectorDAO
from demostration_solution.dao.genre import GenreDAO
from demostration_solution.dao.model.director import Director
from demostration_solution.dao.model.genre import Genre
from demostration_solution.dao.model.movie import Movie
from demostration_solution.dao.movie import MovieDAO

@pytest.fixture
def director_dao():
    director_dao = DirectorDAO(None)

    dir1 = Director(id=1, name='Ivan')
    dir2 = Director(id=2, name='Fedor')

    director_dao.get_one = MagicMock(return_value=dir1)
    director_dao.get_all = MagicMock(return_value=[dir1, dir2])
    director_dao.create = MagicMock(return_value=dir1)
    director_dao.delete = MagicMock()
    director_dao.update = MagicMock()
    return director_dao


@pytest.fixture
def genre_dao():
    genre_dao = GenreDAO(None)

    genre_1 = Genre(id=1, name='Comedy')
    genre_2 = Genre(id=2, name='Drama')

    genre_dao.get_one = MagicMock(return_value=genre_1)
    genre_dao.get_all = MagicMock(return_value=[genre_1, genre_2])
    genre_dao.create = MagicMock(return_value=genre_1)
    genre_dao.delete = MagicMock()
    genre_dao.update = MagicMock()

    return genre_dao


@pytest.fixture
def movie_dao():
    movie_dao = MovieDAO(None)

    mov1 = Movie(id=1, title='title 1', description='Description 1', year=2000)
    mov2 = Movie(id=2, title='title 2', description='Description 2', year=2001)

    movie_dao.get_one = MagicMock(return_value=mov1)
    movie_dao.get_all = MagicMock(return_value=[mov1, mov2])
    movie_dao.create = MagicMock(return_value=mov1)
    movie_dao.delete = MagicMock
    movie_dao.update = MagicMock
    return movie_dao