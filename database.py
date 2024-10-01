import subprocess
# Mysql-connector
try:
    from mysql.connector import *
    print('mysql.connector already installed')
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

# film_window.py
def get_films_informations(id):
    # Cursor creation
    cursor = connection.cursor()
    # Get film infos by his id
    query = "SELECT * FROM movies WHERE id = %s"
    cursor.execute(query, (id,))
    # Stock all the films information in a list
    film_infos = cursor.fetchone()
    # Close the cursor
    cursor.close()
    return film_infos

def get_category_from_id(id):
    # Cursor creation
    cursor = connection.cursor()
    # Get category name by his id
    query = "SELECT name FROM categories WHERE id = %s"
    cursor.execute(query, (id,))
    # Stock all the films information in a list
    category_name = cursor.fetchone()
    # Close the cursor
    cursor.close()
    return category_name

# Function to insert a comment and rating for a movie
def insert_comment_and_rating(movie_id, comment, rating):
    cursor = connection.cursor()
    query = """
    INSERT INTO commentaries (commentar, rate, movie_id)
    VALUES (%s, %s, %s)
    """
    cursor.execute(query, (comment, rating, movie_id))
    connection.commit()
    cursor.close()