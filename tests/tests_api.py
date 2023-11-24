import unittest
from fastapi.testclient import TestClient
from src.main import app
from src.config.connexion import get_db


class BaseTestFastAPI(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.client = TestClient(app)


class TestCommentaires(BaseTestFastAPI):
    def test_add_comment(self):
        comment_data = {
            "date_publication_commentaire": "2011-11-20T22:32:46.310Z",
            "contenu_commentaire": "Testing contents",
            "titre_commentaire": "Testing contents",
            "id_client": 2,
            "id_ouvrage": 1,
        }
        response = self.client.post("/commentaires", json=comment_data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), comment_data)


if __name__ == "__main__":
    unittest.main()
