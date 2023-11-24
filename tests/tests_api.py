import unittest
from fastapi.testclient import TestClient
from src.main import app
from src.config.connexion import get_db


class BaseTestFastAPI(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.client = TestClient(app)


# class TestFastAPIWithDependencies(BaseTestFastAPI):
#     def test_route_with_dependency(self):
#         response = self.client.get("/items/42")
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(response.json(), {"item_id": 42})


if __name__ == "__main__":
    unittest.main()
