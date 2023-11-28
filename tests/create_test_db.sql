CREATE DATABASE `test` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci */;

-- test.client definition

CREATE TABLE `client` (
  `id_client` int(11) NOT NULL AUTO_INCREMENT,
  `nom_client` varchar(255) NOT NULL,
  `prenom_client` varchar(255) NOT NULL,
  `email_client` varchar(255) NOT NULL,
  `telephone_client` varchar(20) NOT NULL,
  `preferences_client` varchar(255) NOT NULL,
  `adresse_livraison_client` varchar(255) NOT NULL,
  `adresse_facturation_client` varchar(255) NOT NULL,
  PRIMARY KEY (`id_client`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;


-- test.ouvrage definition

CREATE TABLE `ouvrage` (
  `id_ouvrage` int(11) NOT NULL AUTO_INCREMENT,
  `titre_ouvrage` varchar(255) NOT NULL,
  `auteur_ouvrage` varchar(255) NOT NULL,
  `isbn_ouvrage` varchar(20) NOT NULL,
  `langue_ouvrage` varchar(20) NOT NULL,
  `prix_ouvrage` decimal(10,0) NOT NULL,
  `date_parution_ouvrage` date NOT NULL,
  `categorie_ouvrage` varchar(255) NOT NULL,
  `date_disponibilite_libraire_ouvrage` date NOT NULL,
  `date_disponibilite_particulier_ouvrage` date NOT NULL,
  `image_ouvrage` varchar(255) NOT NULL,
  `table_des_matieres_ouvrage` varchar(255) NOT NULL,
  `mot_cle_ouvrage` varchar(255) NOT NULL,
  `description_ouvrage` varchar(255) NOT NULL,
  PRIMARY KEY (`id_ouvrage`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- test.theme definition

CREATE TABLE `theme` (
  `id_theme` int(11) NOT NULL AUTO_INCREMENT,
  `nom_theme` varchar(255) NOT NULL,
  PRIMARY KEY (`id_theme`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;


-- test.theme_ouvrage definition

CREATE TABLE `theme_ouvrage` (
  `id_ouvrage` int(11) NOT NULL,
  `id_theme` int(11) NOT NULL,
  PRIMARY KEY (`id_ouvrage`,`id_theme`),
  KEY `id_theme` (`id_theme`),
  CONSTRAINT `theme_ouvrage_ibfk_1` FOREIGN KEY (`id_ouvrage`) REFERENCES `ouvrage` (`id_ouvrage`),
  CONSTRAINT `theme_ouvrage_ibfk_2` FOREIGN KEY (`id_theme`) REFERENCES `theme` (`id_theme`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- test.commentaire definition

CREATE TABLE `commentaire` (
  `id_commentaire` int(11) NOT NULL AUTO_INCREMENT,
  `date_publication_commentaire` date NOT NULL,
  `contenu_commentaire` varchar(255) NOT NULL,
  `titre_commentaire` varchar(255) NOT NULL,
  `id_client` int(11) NOT NULL,
  `id_ouvrage` int(11) NOT NULL,
  PRIMARY KEY (`id_commentaire`),
  KEY `id_client` (`id_client`),
  KEY `id_ouvrage` (`id_ouvrage`),
  CONSTRAINT `commentaire_ibfk_1` FOREIGN KEY (`id_client`) REFERENCES `client` (`id_client`),
  CONSTRAINT `commentaire_ibfk_2` FOREIGN KEY (`id_ouvrage`) REFERENCES `ouvrage` (`id_ouvrage`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;




INSERT INTO test.client (nom_client,prenom_client,email_client,telephone_client,preferences_client,adresse_livraison_client,adresse_facturation_client) VALUES
	 ('Dubois','Marie','marie.dubois@example.com','+33 6 12 34 56 78','Produits bio','12 Rue des Fleurs, 75001 Paris','12 Rue des Fleurs, 75001 Paris'),
	 ('Martin','Jean','jean.martin@example.com','+33 6 23 45 67 89','Livraisons rapides','24 Avenue des Arbres, 69002 Lyon','24 Avenue des Arbres, 69002 Lyon'),
	 ('Lefevre','Sophie','sophie.lefevre@example.com','+33 6 34 56 78 90','Promotions','36 Rue des Montagnes, 31000 Toulouse','36 Rue des Montagnes, 31000 Toulouse'),
	 ('Dupont','Pierre','pierre.dupont@example.com','+33 6 45 67 89 01','Service clientèle','48 Boulevard des Océans, 44000 Nantes','48 Boulevard des Océans, 44000 Nantes'),
	 ('Robert','Emilie','emilie.robert@example.com','+33 6 56 78 90 12','Articles de luxe','60 Avenue des Champs, 13008 Marseille','60 Avenue des Champs, 13008 Marseille'),
	 ('Moreau','Luc','luc.moreau@example.com','+33 6 67 89 01 23','Eco-friendly','72 Rue des Collines, 59000 Lille','72 Rue des Collines, 59000 Lille'),
	 ('Girard','Isabelle','isabelle.girard@example.com','+33 6 78 90 12 34','Livraisons internationales','84 Avenue des Rivières, 67000 Strasbourg','84 Avenue des Rivières, 67000 Strasbourg'),
	 ('Thomas','Paul','paul.thomas@example.com','+33 6 89 01 23 45','Articles personnalisés','96 Boulevard des Forêts, 33000 Bordeaux','96 Boulevard des Forêts, 33000 Bordeaux'),
	 ('Petit','Antoine','antoine.petit@example.com','+33 6 90 12 34 56','Remises fréquentes','108 Rue des Monts, 49000 Angers','108 Rue des Monts, 49000 Angers'),
	 ('Leroy','Catherine','catherine.leroy@example.com','+33 6 01 23 45 67','Nouveautés','120 Avenue des Vallées, 57000 Metz','120 Avenue des Vallées, 57000 Metz');
INSERT INTO test.client (nom_client,prenom_client,email_client,telephone_client,preferences_client,adresse_livraison_client,adresse_facturation_client) VALUES
	 ('Roux','François','francois.roux@example.com','+33 6 12 34 56 78','Produits locaux','132 Rue des Collines, 38000 Grenoble','132 Rue des Collines, 38000 Grenoble'),
	 ('Garnier','Marion','marion.garnier@example.com','+33 6 23 45 67 89','Mode éthique','144 Avenue des Plages, 20000 Ajaccio','144 Avenue des Plages, 20000 Ajaccio'),
	 ('Masson','David','david.masson@example.com','+33 6 34 56 78 90','Articles de sport','156 Rue des Vignes, 34000 Montpellier','156 Rue des Vignes, 34000 Montpellier'),
	 ('Guerin','Elise','elise.guerin@example.com','+33 6 45 67 89 01','Électronique','168 Boulevard des Lacs, 59000 Dunkerque','168 Boulevard des Lacs, 59000 Dunkerque'),
	 ('Fournier','Thierry','thierry.fournier@example.com','+33 6 56 78 90 12','Accessoires de maison','180 Rue des Châteaux, 37000 Tours','180 Rue des Châteaux, 37000 Tours');




INSERT INTO test.ouvrage (titre_ouvrage,auteur_ouvrage,isbn_ouvrage,langue_ouvrage,prix_ouvrage,date_parution_ouvrage,categorie_ouvrage,date_disponibilite_libraire_ouvrage,date_disponibilite_particulier_ouvrage,image_ouvrage,table_des_matieres_ouvrage,mot_cle_ouvrage,description_ouvrage) VALUES
	 ('Les Misérables','Victor Hugo','978-2070416020','français',25,'1862-03-15','Roman','2023-12-01','2023-12-15','url_de_l_image','Partie 1: Fantine','épopée, rédemption, misère','Les Misérables est un chef-d''œuvre de la littérature française qui suit les vies interconnectées de plusieurs personnages à travers les tumultes de la France du XIXe siècle.'),
	 ('To Kill a Mockingbird','Harper Lee','978-0061120084','anglais',20,'1960-07-11','Fiction','2023-12-05','2023-12-20','url_de_l_image','Chapter 1: A Tired Old Town','racisme, justice, enfance','To Kill a Mockingbird aborde les thèmes du racisme et de l''injustice à travers les yeux de Scout Finch, une jeune fille du sud des États-Unis.'),
	 ('Pride and Prejudice','Jane Austen','978-1503290562','anglais',13,'1813-01-28','Romance','2023-12-10','2023-12-25','url_de_l_image','Volume 1: It is a truth universally acknowledged','amour, classe sociale, satire','Pride and Prejudice est une satire sociale qui explore les relations amoureuses au début du XIXe siècle en Angleterre.'),
	 ('The Great Gatsby','F. Scott Fitzgerald','978-0743273565','anglais',15,'1925-04-10','Fiction','2023-12-15','2023-12-30','url_de_l_image','Chapter 1: In my younger and more vulnerable years','rébellion, illusion, richesse','The Great Gatsby offre un regard critique sur l''illusion de la richesse et de l''amour dans les années folles américaines.'),
	 ('One Hundred Years of Solitude','Gabriel García Márquez','978-0061120084','espagnol',23,'1967-05-30','Magical Realism','2023-12-20','2024-01-05','url_de_l_image','Cien años de soledad','réalisme magique, génération, solitude','One Hundred Years of Solitude est un chef-d''œuvre du réalisme magique qui raconte l''histoire de la famille Buendía sur plusieurs générations.'),
	 ('The Hobbit','J.R.R. Tolkien','978-0547928227','anglais',18,'1937-09-21','Fantasy','2024-01-01','2024-01-15','url_de_l_image','Chapter 1: An Unexpected Party','aventure, hobbits, dragon','The Hobbit, ou There and Back Again, suit les aventures de Bilbo Baggins alors qu''il se joint à une quête pour récupérer un trésor gardé par le dragon Smaug.'),
	 ('Brave New World','Aldous Huxley','978-0060850524','anglais',17,'1932-10-27','Science-fiction','2024-01-05','2024-01-20','url_de_l_image','Chapter 1: A SQUAT grey building','dystopie, contrôle social, technologie','Brave New World dépeint une société future dystopique où la technologie et le contrôle social ont atteint des extrêmes inquiétants.'),
	 ('The Catcher in the Rye','J.D. Salinger','978-0241950425','anglais',14,'1951-07-16','Fiction','2024-01-10','2024-01-25','url_de_l_image','Chapter 1: If you really want to hear','adolescence, désillusion, rébellion','The Catcher in the Rye suit les pensées et les aventures de Holden Caulfield, un adolescent rebelle qui cherche du sens dans un monde qu''il trouve hypocrite.'),
	 ('The Lord of the Flies','William Golding','978-0571191475','anglais',14,'1954-09-17','Fiction','2024-01-15','2024-01-30','url_de_l_image','Chapter 1: The Sound of the Shell','nature humaine, survie, société','The Lord of the Flies explore la dégénérescence de la société et de la nature humaine lorsque des enfants se retrouvent isolés sur une île déserte.'),
	 ('The Road','Cormac McCarthy','978-0307387899','anglais',20,'2006-09-26','Post-apocalyptic Fiction','2024-02-01','2024-02-15','url_de_l_image','Part 1: The Fire','apocalypse, père-fils, survie','The Road suit un père et son fils dans un monde post-apocalyptique, luttant pour survivre tout en préservant leur humanité.');
INSERT INTO test.ouvrage (titre_ouvrage,auteur_ouvrage,isbn_ouvrage,langue_ouvrage,prix_ouvrage,date_parution_ouvrage,categorie_ouvrage,date_disponibilite_libraire_ouvrage,date_disponibilite_particulier_ouvrage,image_ouvrage,table_des_matieres_ouvrage,mot_cle_ouvrage,description_ouvrage) VALUES
	 ('The Alchemist','Paulo Coelho','978-0061120084','anglais',16,'1988-01-01','Fiction','2024-02-05','2024-02-20','url_de_l_image','Part 1: The Boy''s Name','quête, destin, spiritualité','The Alchemist suit Santiago, un jeune berger, dans sa quête pour découvrir son destin personnel et réaliser ses rêves.'),
	 ('Le Nom du Vent','Patrick Rothfuss','978-2352940905','français',26,'2007-03-27','Fantasy','2023-12-01','2023-12-15','url_de_l_image','Partie 1: L''Enfance à Trouver','magie, aventure, conte','Le Nom du Vent est le premier tome de la trilogie du Roi tueur. Il raconte l''histoire de Kvothe, un musicien et magicien légendaire, et ses aventures à travers le royaume.'),
	 ('Sapiens: Une brève histoire de l''humanité','Yuval Noah Harari','978-2226433961','français',22,'2011-04-28','Histoire','2023-12-05','2023-12-20','url_de_l_image','Partie 1: La Révolution cognitive','histoire, évolution, société','Sapiens explore l''histoire de l''humanité, de l''émergence des Homo sapiens à la révolution agricole et au-delà. Une perspective fascinante sur l''évolution de notre espèce.'),
	 ('To Kill a Mockingbird','Harper Lee','978-0061120084','anglais',15,'1960-07-11','Roman','2023-12-10','2023-12-25','url_de_l_image','Part 1: Maycomb, Alabama','justice, préjugés, enfance','To Kill a Mockingbird explore les thèmes de la justice, de la compassion et du racisme dans le sud des États-Unis à travers les yeux de la jeune Scout Finch.'),
	 ('Une femme','Annie Ernaux','978-2070381552','français',18,'1987-08-26','Autobiographie','2024-01-10','2024-01-25','url_de_l_image','Chapitre 1: L''histoire d''une vie','autobiographie, mémoire, identité','Une femme est une œuvre autobiographique où Annie Ernaux explore sa propre histoire, ses expériences, et les changements sociaux au fil des années. Une réflexion poignante sur la vie d''une femme contemporaine.');

INSERT INTO test.theme (nom_theme) VALUES
	 ('Amour et Relations'),
	 ('Aventure'),
	 ('Mystère et Suspense'),
	 ('Fantasy'),
	 ('LGBTQ'),
	 ('Histoire et Historique'),
	 ('Drame'),
	 ('Thriller'),
	 ('Horreur'),
	 ('Comédie');
	
INSERT INTO test.theme (nom_theme) VALUES
	 ('Développement personnel'),
	 ('Enquête et Crime'),
	 ('Nature et Environnement'),
	 ('Voyages et Exploration'),
	 ('Philosophie');
	
INSERT INTO test.theme_ouvrage (id_ouvrage,id_theme) VALUES
	 (14,1),
	 (5,2),
	 (10,3),
	 (8,4),
	 (15,5),
	 (6,6),
	 (2,7),
	 (4,8),
	 (11,9),
	 (7,10);
INSERT INTO test.theme_ouvrage (id_ouvrage,id_theme) VALUES
	 (4,11),
	 (1,12),
	 (13,12),
	 (9,13),
	 (3,14);

	

INSERT INTO test.commentaire (date_publication_commentaire,contenu_commentaire,titre_commentaire,id_client,id_ouvrage) VALUES
	 ('2023-11-13','Une lecture agréable et légère. Idéal pour se détendre après une journée chargée.','Agréable',15,15),
	 ('2023-11-14','J''ai trouvé le message de ce livre très inspirant. Ça m''a fait réfléchir sur ma propre vie.','Inspirant',14,13),
	 ('2023-11-15','Une lecture rapide et palpitante. Parfait pour les amateurs d''action.','Palpitant',13,11),
	 ('2023-11-16','Ce livre m''a fait rire et pleurer. Une expérience émotionnelle complète.','Émotionnellement riche',12,4),
	 ('2023-11-17','L''auteur a une façon unique de jouer avec les mots. J''ai apprécié chaque page.','Jouer avec les mots',11,8),
	 ('2023-11-18','Un récit magnifiquement écrit. Les descriptions étaient tellement vivantes.','Magnifiquement écrit',10,2),
	 ('2023-11-19','J''ai été émotionnellement bouleversé par ce livre. Une lecture vraiment puissante.','Émotionnellement bouleversant',9,14),
	 ('2023-11-20','Une fin surprenante qui a complètement changé ma perspective sur toute l''histoire.','Fin surprenante',8,6),
	 ('2023-11-21','J''ai trouvé les personnages extrêmement bien développés. Le réalisme les rendait très attachants.','Personnages attachants',7,9),
	 ('2023-11-28','n classique intemporel. Les thèmes abordés restent pertinents même aujourd''hui.','Classique',6,1);

INSERT INTO test.commentaire (date_publication_commentaire,contenu_commentaire,titre_commentaire,id_client,id_ouvrage) VALUES
	 ('2023-11-23','Une lecture légère et divertissante. Parfait pour se détendre.','Divertissant',5,10),
	 ('2023-11-24','L''histoire était pleine de rebondissements inattendus. Je n''ai pas pu le lâcher!','Captivant',4,5),
	 ('2023-11-25','Ce livre m''a fait réfléchir sur la condition humaine. Une lecture profonde et émouvante.','Réflexions profondes',3,12),
	 ('2023-11-26','Un chef-d''œuvre absolu. L''auteur a su créer un monde fascinant et original.','Chef-d''œuvre',2,7),
	 ('2023-11-27',' J''ai adoré ce livre! L''intrigue était captivante et les personnages bien développés.','Excellent',1,3);