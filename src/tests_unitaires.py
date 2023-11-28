# Third party imports
from fastapi.testclient import TestClient
import unittest

# Local imports
from main import app


class BaseTestFastAPI(unittest.TestCase):
    """Necessaire pour créer la connection avec l'application, cette classe sera héritée par chaque classe de tests."""

    @classmethod
    def setUpClass(cls):
        cls.client = TestClient(app)


class TestClients(BaseTestFastAPI):
    """Class pour tester le CRUD du router pour le table client."""

    def test_get_client_by_id(self):
        """Tester la recherche par ID client"""

        test_response = self.client.get("/information_client/1")
        expected_response = {
            "info client": {
                "email_client": "marie.dubois@example.com",
                "telephone_client": "+33 6 12 34 56 78",
                "prenom_client": "Marie",
                "adresse_livraison_client": "12 Rue des Fleurs, 75001 Paris",
                "nom_client": "Dubois",
                "id_client": 1,
                "preferences_client": "Produits bio",
                "adresse_facturation_client": "12 Rue des Fleurs, 75001 Paris",
            }
        }

        self.assertEqual(test_response.status_code, 200)
        self.assertEqual(test_response.json(), expected_response)

    def test_add_cleint(self):
        """Tester l'ajoute d'un client."""

        client_data = {
            "nom_client": "Test Client Nom",
            "prenom_client": "Test Client Prenom",
            "email_client": "Test Client Email",
            "telephone_client": "Test Client Tel",
            "preferences_client": "Test Client Preferences",
            "adresse_livraison_client": "Test Client Adresse Livraison",
            "adresse_facturation_client": "Test Client Adresse Facturation",
        }
        test_response = self.client.post("/inscription/", json=client_data)
        expected_response = {
            "nom_client": "Test Client Nom",
            "prenom_client": "Test Client Prenom",
            "email_client": "Test Client Email",
            "telephone_client": "Test Client Tel",
            "preferences_client": "Test Client Preferences",
            "adresse_livraison_client": "Test Client Adresse Livraison",
            "adresse_facturation_client": "Test Client Adresse Facturation",
        }

        self.assertEqual(test_response.status_code, 201)
        self.assertEqual(test_response.json(), expected_response)

    def test_update_client(self):
        """Tester la mise à jour des données d'un client."""

        update_data = {
            "nom_client": "Test Name Change",
            "telephone_client": "+1 11 11 11 11 11",
        }
        test_response = self.client.patch("/modification_client/5", json=update_data)
        expected_response = {
            "nom_client": "Test Name Change",
            "prenom_client": "Emilie",
            "email_client": "emilie.robert@example.com",
            "telephone_client": "+1 11 11 11 11 11",
            "preferences_client": "Articles de luxe",
            "adresse_livraison_client": "60 Avenue des Champs, 13008 Marseille",
            "adresse_facturation_client": "60 Avenue des Champs, 13008 Marseille",
        }

        self.assertEqual(test_response.status_code, 200)
        self.assertEqual(test_response.json(), expected_response)

    def test_delete_client(self):
        """Test pour vérifier la route pour supprimer un client"""

        test_response = self.client.delete("/suppression_client/10")
        expected_response = {
            "personne supprimée": {
                "email_client": "catherine.leroy@example.com",
                "prenom_client": "Catherine",
                "adresse_livraison_client": "120 Avenue des Vallées, 57000 Metz",
                "telephone_client": "+33 6 01 23 45 67",
                "preferences_client": "Nouveautés",
                "adresse_facturation_client": "120 Avenue des Vallées, 57000 Metz",
                "nom_client": "Leroy",
                "id_client": 10,
            }
        }

        self.assertEqual(test_response.status_code, 200)
        self.assertEqual(test_response.json(), expected_response)


class TestCommentaires(BaseTestFastAPI):
    """Cette classe contient tous les tests unitaires pour gérer le table commentaire."""

    def test_get_comment(self):
        """Test pour vérifier la route pour chercher un commentaire par ID"""

        test_response = self.client.get("/commentaires/1")
        expected_response = {
            "id_commentaire": 1,
            "date_publication_commentaire": "2023-11-13T00:00:00",
            "contenu_commentaire": "Une lecture agréable et légère. Idéal pour se détendre après une journée chargée.",
            "titre_commentaire": "Agréable",
            "id_client": 15,
            "id_ouvrage": 15,
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

    def test_add_comment(self):
        """Test pour vérifier l'ajoute d'un commentaire."""

        comment_data = {
            "date_publication_commentaire": "2023-11-28T14:21:20.833Z",
            "contenu_commentaire": "New Comment Content",
            "titre_commentaire": "New Comment Title",
            "id_client": 1,
            "id_ouvrage": 10,
        }
        test_response = self.client.post("/commentaires", json=comment_data)
        expected_response = {
            "id_commentaire": 16,
            "date_publication_commentaire": "2023-11-28T00:00:00",
            "contenu_commentaire": "New Comment Content",
            "titre_commentaire": "New Comment Title",
            "id_client": 1,
            "id_ouvrage": 10,
        }

        self.assertEqual(test_response.status_code, 201)
        self.assertEqual(test_response.json(), expected_response)

    def test_delete_comment(self):
        """Test pour vérifier la route pour supprimer un commentaire"""

        test_response = self.client.delete("/commentaires/15")
        expected_response = "Commentaire supprimé."

        self.assertEqual(test_response.status_code, 201)
        self.assertEqual(test_response.json(), expected_response)


class TestOuvrages(BaseTestFastAPI):
    """Classe pour tester le CRUD pour le table ouvrage"""

    def test_get_ouvrage(self):
        """Test pour retrouver un ouvrage par son id"""
        response = self.client.get("/ouvrages/2")

        excpected = {
            "id_ouvrage": 2,
            "isbn_ouvrage": "978-0061120084",
            "prix_ouvrage": 20,
            "categorie_ouvrage": "Fiction",
            "date_disponibilite_particulier_ouvrage": "2023-12-20",
            "table_des_matieres_ouvrage": "Chapter 1: A Tired Old Town",
            "description_ouvrage": "To Kill a Mockingbird aborde les thèmes du racisme et de l'injustice à travers les yeux de Scout Finch, une jeune fille du sud des États-Unis.",
            "titre_ouvrage": "To Kill a Mockingbird",
            "auteur_ouvrage": "Harper Lee",
            "langue_ouvrage": "anglais",
            "date_parution_ouvrage": "1960-07-11",
            "date_disponibilite_libraire_ouvrage": "2023-12-05",
            "image_ouvrage": "url_de_l_image",
            "mot_cle_ouvrage": "racisme, justice, enfance",
        }

        self.maxDiff = None
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), excpected)

    def test_add_ouvrage(self):
        """Test ajout d'un ouvrage."""
        ouvrage_data = {
            "titre_ouvrage": "TEST TITLE",
            "auteur_ouvrage": "TEST AUTHOR",
            "isbn_ouvrage": "000-0000000000",
            "langue_ouvrage": "anglais",
            "prix_ouvrage": 0.0,
            "date_parution_ouvrage": "2000-01-01",
            "categorie_ouvrage": "Fiction",
            "date_disponibilite_libraire_ouvrage": "2000-01-01",
            "date_disponibilite_particulier_ouvrage": "2000-01-01",
            "image_ouvrage": "url_de_l_image",
            "table_des_matieres_ouvrage": "TEST SUMMARY",
            "mot_cle_ouvrage": "TEST",
            "description_ouvrage": "TEST",
        }

        expected_response = {
            "titre_ouvrage": "TEST TITLE",
            "auteur_ouvrage": "TEST AUTHOR",
            "isbn_ouvrage": "000-0000000000",
            "langue_ouvrage": "anglais",
            "prix_ouvrage": 0.0,
            "date_parution_ouvrage": "2000-01-01",
            "categorie_ouvrage": "Fiction",
            "date_disponibilite_libraire_ouvrage": "2000-01-01",
            "date_disponibilite_particulier_ouvrage": "2000-01-01",
            "image_ouvrage": "url_de_l_image",
            "table_des_matieres_ouvrage": "TEST SUMMARY",
            "mot_cle_ouvrage": "TEST",
            "description_ouvrage": "TEST",
        }
        response = self.client.post("/ouvrage", json=ouvrage_data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), expected_response)

    def test_update_ouvrage(self):
        """Test pour vérification de la mise à jour des ouvrages"""

        response = self.client.patch(
            "/ouvrage/1",
            json={"isbn_ouvrage": "000-0000000000", "langue_ouvrage": "Python"},
        )
        excpected = {
            "titre_ouvrage": "Les Misérables",
            "auteur_ouvrage": "Victor Hugo",
            "isbn_ouvrage": "000-0000000000",
            "langue_ouvrage": "Python",
            "prix_ouvrage": 25,
            "date_parution_ouvrage": "1862-03-15",
            "categorie_ouvrage": "Roman",
            "date_disponibilite_libraire_ouvrage": "2023-12-01",
            "date_disponibilite_particulier_ouvrage": "2023-12-15",
            "image_ouvrage": "url_de_l_image",
            "table_des_matieres_ouvrage": "Partie 1: Fantine",
            "mot_cle_ouvrage": "épopée, rédemption, misère",
            "description_ouvrage": "Les Misérables est un chef-d'œuvre de la littérature française qui suit les vies interconnectées de plusieurs personnages à travers les tumultes de la France du XIXe siècle.",
        }

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), excpected)

    def test_delete_ouvrage(self):
        """Test pour vérifier la supression d'un ouvrage."""

        test_response = self.client.delete("/ouvrage/5")
        expected_response = {
            "Ouvrage supprimé: ": {
                "isbn_ouvrage": "978-0061120084",
                "categorie_ouvrage": "Magical Realism",
                "prix_ouvrage": 23,
                "date_disponibilite_particulier_ouvrage": "2024-01-05",
                "description_ouvrage": "One Hundred Years of Solitude est un chef-d'œuvre du réalisme magique qui raconte l'histoire de la famille Buendía sur plusieurs générations.",
                "id_ouvrage": 5,
                "table_des_matieres_ouvrage": "Cien años de soledad",
                "auteur_ouvrage": "Gabriel García Márquez",
                "langue_ouvrage": "espagnol",
                "date_parution_ouvrage": "1967-05-30",
                "date_disponibilite_libraire_ouvrage": "2023-12-20",
                "image_ouvrage": "url_de_l_image",
                "titre_ouvrage": "One Hundred Years of Solitude",
                "mot_cle_ouvrage": "réalisme magique, génération, solitude",
                "commentaires": [],
                "themes": {},
            }
        }

        self.assertEqual(test_response.status_code, 200)
        self.assertEqual(test_response.json(), expected_response)

    def test_search_one_param(self):
        """Test pour retrouver un ouvrage par la recherche d'un paramètre: auteur, catégorie, langue, mot clé ou titre."""
        response = self.client.get("/recherche_unitaire/auteur/ernaux")

        excpected = [
            {
                "id_ouvrage": 15,
                "isbn_ouvrage": "978-2070381552",
                "prix_ouvrage": 18,
                "categorie_ouvrage": "Autobiographie",
                "date_disponibilite_particulier_ouvrage": "2024-01-25",
                "table_des_matieres_ouvrage": "Chapitre 1: L'histoire d'une vie",
                "description_ouvrage": "Une femme est une œuvre autobiographique où Annie Ernaux explore sa propre histoire, ses expériences, et les changements sociaux au fil des années. Une réflexion poignante sur la vie d'une femme contemporaine.",
                "titre_ouvrage": "Une femme",
                "auteur_ouvrage": "Annie Ernaux",
                "langue_ouvrage": "français",
                "date_parution_ouvrage": "1987-08-26",
                "date_disponibilite_libraire_ouvrage": "2024-01-10",
                "image_ouvrage": "url_de_l_image",
                "mot_cle_ouvrage": "autobiographie, mémoire, identité",
            }
        ]

        self.maxDiff = None
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), excpected)

    def test_search_two_params(self):
        """Test pour retrouver un ouvrage par la recherche de deux paramètres: auteur, catégorie, langue, mot clé ou titre."""
        response = self.client.get("/recherche_double/auteur/co/titre/The")

        excpected = [
            {
                "id_ouvrage": 4,
                "isbn_ouvrage": "978-0743273565",
                "prix_ouvrage": 15,
                "categorie_ouvrage": "Fiction",
                "date_disponibilite_particulier_ouvrage": "2023-12-30",
                "table_des_matieres_ouvrage": "Chapter 1: In my younger and more vulnerable years",
                "description_ouvrage": "The Great Gatsby offre un regard critique sur l'illusion de la richesse et de l'amour dans les années folles américaines.",
                "titre_ouvrage": "The Great Gatsby",
                "auteur_ouvrage": "F. Scott Fitzgerald",
                "langue_ouvrage": "anglais",
                "date_parution_ouvrage": "1925-04-10",
                "date_disponibilite_libraire_ouvrage": "2023-12-15",
                "image_ouvrage": "url_de_l_image",
                "mot_cle_ouvrage": "rébellion, illusion, richesse",
            },
            {
                "id_ouvrage": 10,
                "isbn_ouvrage": "978-0307387899",
                "prix_ouvrage": 20,
                "categorie_ouvrage": "Post-apocalyptic Fiction",
                "date_disponibilite_particulier_ouvrage": "2024-02-15",
                "table_des_matieres_ouvrage": "Part 1: The Fire",
                "description_ouvrage": "The Road suit un père et son fils dans un monde post-apocalyptique, luttant pour survivre tout en préservant leur humanité.",
                "titre_ouvrage": "The Road",
                "auteur_ouvrage": "Cormac McCarthy",
                "langue_ouvrage": "anglais",
                "date_parution_ouvrage": "2006-09-26",
                "date_disponibilite_libraire_ouvrage": "2024-02-01",
                "image_ouvrage": "url_de_l_image",
                "mot_cle_ouvrage": "apocalypse, père-fils, survie",
            },
            {
                "id_ouvrage": 11,
                "isbn_ouvrage": "978-0061120084",
                "prix_ouvrage": 16,
                "categorie_ouvrage": "Fiction",
                "date_disponibilite_particulier_ouvrage": "2024-02-20",
                "table_des_matieres_ouvrage": "Part 1: The Boy's Name",
                "description_ouvrage": "The Alchemist suit Santiago, un jeune berger, dans sa quête pour découvrir son destin personnel et réaliser ses rêves.",
                "titre_ouvrage": "The Alchemist",
                "auteur_ouvrage": "Paulo Coelho",
                "langue_ouvrage": "anglais",
                "date_parution_ouvrage": "1988-01-01",
                "date_disponibilite_libraire_ouvrage": "2024-02-05",
                "image_ouvrage": "url_de_l_image",
                "mot_cle_ouvrage": "quête, destin, spiritualité",
            },
        ]

        self.maxDiff = None
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), excpected)


if __name__ == "__main__":
    unittest.main()
