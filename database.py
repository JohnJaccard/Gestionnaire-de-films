from mysql.connector import *


# connection à la db
connection = connect(
    host="localhost",
    user="root",
    password="Pa$$w0rd",
    database="netfloux"
)


# main.py

def get_films_from_category(category_id):
    # récup info des films de la catégorie
    cursor = connection.cursor()
    # Requête pour récupérer le nom du film par ID
    query = "SELECT * FROM movies WHERE category_id = %s"
    cursor.execute(query, (category_id,))
    films_to_diplay = cursor.fetchall()
    # Fermeture de la connexion
    cursor.close()
    return films_to_diplay


def get_categories():
    # récup info des catégories selectionné
    cursor = connection.cursor()
    # Requête pour récupérer le nom du film par ID
    query = "SELECT * FROM categories"
    cursor.execute(query)
    categories = cursor.fetchall()
    # Fermeture de la connexion
    cursor.close()
    return categories

#film_window
def get_films_informations(id):
    #récup info du film selectionné
    cursor = connection.cursor()
    # Requête pour récupérer le nom du film par ID
    query = "SELECT * FROM movies WHERE id = %s"
    cursor.execute(query, (id,))
    film_infos = cursor.fetchone()
    film_name = film_infos[1]
    # Fermeture de la connexion
    cursor.close()
    return film_name
