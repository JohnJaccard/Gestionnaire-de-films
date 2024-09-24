import subprocess
try:
    from mysql.connector import *
    print('connector ok')
except:
    subprocess.run('pip install mysql-connector-python', shell=True)


# Database connection
connection = connect(
    host="localhost",
    user="root",
    password="Pa$$w0rd",
    database="netfloux"
)


# main.py functions

def get_films_from_category(category_id):
    # Cursor creation
    cursor = connection.cursor()
    # Get films from category
    query = "SELECT * FROM movies WHERE category_id = %s"
    cursor.execute(query, (category_id,))
    films_to_diplay = cursor.fetchall()
    # Close the cursor
    cursor.close()
    return films_to_diplay


def get_categories():
    # Cursor creation
    cursor = connection.cursor()
    # Get all categories
    query = "SELECT * FROM categories"
    cursor.execute(query)
    categories = cursor.fetchall()
    # Close the cursor
    cursor.close()
    return categories

#film_window
def get_films_informations(id):
    # Cursor creation
    cursor = connection.cursor()
    # Get film infos by his id
    query = "SELECT * FROM movies WHERE id = %s"
    cursor.execute(query, (id,))
    film_infos = cursor.fetchone()
    # Take the name from the infos list
    film_name = film_infos[1]
    # Close the cursor
    cursor.close()
    return film_name
