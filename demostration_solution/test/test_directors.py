import pytest
from demostration_solution.service.director import DirectorService

class TestDirectorService:
    @pytest.fixture(autouse=True)
    def test_director_service(self, director_dao):
        self.director_service = DirectorService(dao=director_dao)


    def test_get_one(self):
        dir_one = self.director_service.get_one(1)
        assert dir_one is not None
        assert dir_one.name == 'Ivan'


    def test_get_all(self):
        dir_all = self.director_service.get_all()
        assert len(dir_all) > 0


    def test_create(self):
        dir_data = {'name': 'Name'}
        new_dir = self.director_service.create(dir_data)
        assert new_dir.id is not None


    def test_update(self):
        self.director_service.update(1)


    def test_delete(self):
        result = self.director_service.delete(1)
        assert result is None