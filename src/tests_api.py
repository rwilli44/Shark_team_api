import unittest
from fastapi.testclient import TestClient
from main import app
from config.connexion import get_db


class BaseTestFastAPI(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.client = TestClient(app)


class TestCommentaires(BaseTestFastAPI):
    def test_get_comment(self):
        """Test pour vérifier la route pour chercher un commentaire par ID"""

        test_response = self.client.get("/commentaires/1")

        expected_response = {
            "id_commentaire": 15,
            "date_publication_commentaire": "2023-11-27T00:00:00",
            "contenu_commentaire": "J'ai adoré ce livre! L'intrigue était captivante et les personnages bien développés.",
            "titre_commentaire": "Excellent",
            "id_client": 1,
            "id_ouvrage": 3,
        }

        self.assertEqual(test_response.status_code, 200)
        self.assertEqual(test_response.json(), expected_response)

    def test_update_comment(self):
        """Test pour vérifier la mise à jour d'un commentaire (UPDATE/patch)."""
        test_response = self.client.patch(
            "/commentaires/10",
            json={
                "contenu_commentaire": "Updated Content",
                "titre_commentaire": "Updated Title",
            },
        )
        expected_response = {
            "id_commentaire": 10,
            "date_publication_commentaire": "2023-11-28T00:00:00",
            "contenu_commentaire": "Updated Content",
            "titre_commentaire": "Updated Title",
            "id_client": 6,
            "id_ouvrage": 1,
        }
        self.assertEqual(test_response.status_code, 200)
        self.assertEqual(test_response.json(), expected_response)

    # def test_add_comment(self):
    #     """Test pour vérifier l'ajoute d'un commentaire."""
    #     comment_data = {
    #         "date_publication_commentaire": "2023-11-26T21:56:14.336Z",
    #         "contenu_commentaire": "Test commentary",
    #         "titre_commentaire": "Test comment",
    #         "id_client": 1,
    #         "id_ouvrage": 1,
    #     }
    #     expected_response = {
    #         "id_commentaire": 16,
    #         "date_publication_commentaire": "2023-11-28T00:00:00",
    #         "contenu_commentaire": "Test commentary",
    #         "titre_commentaire": "Test comment",
    #         "id_client": 1,
    #         "id_ouvrage": 1,
    #     }
    #     response = self.client.post("/commentaires/add", json=comment_data)
    #     self.assertEqual(response.status_code, 201)
    #     self.assertEqual(response.json(), expected_response)

    def test_delete_comment(self):
        """Test pour vérifier la route pour supprimer un commentaire"""
        test_response = self.client.delete("/commentaires/15")
        expected_response = "Commentaire supprimé."
        self.assertEqual(test_response.status_code, 200)
        self.assertEqual(test_response.json(), expected_response)

    def test_comment_was_deleted(self):
        """Test pour vérifier que le commentaire supprimer n'existe plus."""
        test_response = self.client.get("/commentaires/15")

        self.assertEqual(test_response.status_code, 404)


if __name__ == "__main__":
    unittest.main()
