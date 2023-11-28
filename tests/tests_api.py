import unittest
from fastapi.testclient import TestClient
from main import app
from config.connexion import get_db


class BaseTestFastAPI(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.client = TestClient(app)


class TestCommentaires(BaseTestFastAPI):
    def test_add_comment(self):
        comment_data = {
            "date_publication_commentaire": "2023-11-26T21:56:14.336Z",
            "contenu_commentaire": "Test commentary",
            "titre_commentaire": "Test comment",
            "id_client": 1,
            "id_ouvrage": 1,
        }
        expected_response = comment_data = {
            "id_commentaire": 23,  ## need to find a way to not hardcode this or it will fail
            "date_publication_commentaire": "2023-11-26T00:00:00",
            "contenu_commentaire": "Test commentary",
            "titre_commentaire": "Test comment",
            "id_client": 1,
            "id_ouvrage": 1,
        }
        response = self.client.post("/commentaires/add", json=comment_data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(), expected_response)


if __name__ == "__main__":
    unittest.main()
