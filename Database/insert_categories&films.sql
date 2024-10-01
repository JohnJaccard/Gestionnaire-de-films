-- Insertion des catégories (déjà présente dans le script original)
INSERT INTO categories (name) VALUES
('Action'),
('Aventure'),
('Comédie'),
('Drame'),
('Horreur'),
('Science-Fiction'),
('Fantastique'),
('Animation'),
('Documentaire'),
('Romance'),
('Thriller'),
('Policier'),
('Guerre'),
('Western'),
('Musical'),
('Biopic'),
('Historique'),
('Familial'),
('Sport'),
('Mystère');

-- Insertion de films dans la table movies avec description et lien du trailer
INSERT INTO movies (name, duration, watched, minimum_age, streaming_site, release_date, description, trailer_link, category_id) VALUES
('Inception', '02:28:00', 1, 13, 'Netflix', '2010-07-16', 'Un voleur qui infiltre les rêves pour voler des secrets d''entreprise.', 'https://www.youtube.com/watch?v=8hP9D6kZseM', 1),
('The Godfather', '02:55:00', 0, 17, 'Prime Video', '1972-03-24', 'L''histoire de la famille Corleone dans la mafia italienne.', 'https://www.youtube.com/watch?v=sY1S34973zA', 2),
('The Dark Knight', '02:32:00', 1, 13, 'HBO Max', '2008-07-18', 'Batman fait face à son ennemi mortel, le Joker, à Gotham.', 'https://www.youtube.com/watch?v=EXeTwQWrcwY', 1),
('Pulp Fiction', '02:34:00', 1, 17, 'Disney+', '1994-10-14', 'Un ensemble d''histoires criminelles reliées entre elles à Los Angeles.', 'https://www.youtube.com/watch?v=s7EdQ4FqbhY', 3),
('Schindler''s List', '03:15:00', 0, 17, 'Netflix', '1993-12-15', 'L''histoire vraie de l''industriel Oskar Schindler qui sauve des Juifs pendant la Shoah.', 'https://www.youtube.com/watch?v=M5FpB6qDGAE', 4),
('The Lord of the Rings: The Return of the King', '03:21:00', 0, 13, 'Prime Video', '2003-12-17', 'La conclusion épique de la lutte pour détruire l''Anneau unique.', 'https://www.youtube.com/watch?v=r5X-hFf6Bwo', 2),
('Forrest Gump', '02:22:00', 1, 13, 'HBO Max', '1994-07-06', 'L''histoire d''un homme simple qui influence les grands événements du 20e siècle.', 'https://www.youtube.com/watch?v=bLvqoHBptjg', 3),
('Fight Club', '02:19:00', 0, 17, 'Disney+', '1999-10-15', 'Un homme désillusionné crée un club de combat clandestin avec un vendeur de savon.', 'https://www.youtube.com/watch?v=SUXWAEX2jlg', 1),
('The Matrix', '02:16:00', 1, 13, 'Netflix', '1999-03-31', 'Un hacker découvre que la réalité n''est qu''une simulation et se rebelle contre ses créateurs.', 'https://www.youtube.com/watch?v=vKQi3bBA1y8', 5),
('Goodfellas', '02:26:00', 0, 17, 'Prime Video', '1990-09-21', 'L''ascension et la chute d''un mafieux de New York.', 'https://www.youtube.com/watch?v=qo5jJpHtI1Y', 2),
('Indiana Jones and the Last Crusade', '02:07:00', 0, 11, 'Disney+', '1989-05-24', 'Indiana Jones part à la recherche du Saint Graal avec son père.', 'https://www.youtube.com/watch?v=sagmdpkWUqc', 2),
('The Shawshank Redemption', '02:22:00', 1, 13, 'Netflix', '1994-09-23', 'L''histoire d''un homme injustement emprisonné qui trouve l''espoir derrière les barreaux.', 'https://www.youtube.com/watch?v=NmzuHjWmXOc', 4),
('Gladiator', '02:35:00', 0, 17, 'Prime Video', '2000-05-05', 'Un général romain trahi se venge en tant que gladiateur.', 'https://www.youtube.com/watch?v=owK1qxDselE', 1),
('Interstellar', '02:49:00', 1, 13, 'HBO Max', '2014-11-07', 'Un groupe d''astronautes voyage à travers un trou de ver pour sauver l''humanité.', 'https://www.youtube.com/watch?v=zSWdZVtXT7E', 5),
('The Silence of the Lambs', '01:58:00', 0, 17, 'Disney+', '1991-02-14', 'Une jeune enquêtrice du FBI consulte un tueur en série emprisonné pour capturer un autre meurtrier.', 'https://www.youtube.com/watch?v=W6Mm8Sbe__o', 11);
