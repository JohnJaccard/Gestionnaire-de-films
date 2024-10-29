import subprocess
# Mysql-connector
try:
    from mysql.connector import connect
    print('mysql.connector already installed')
except ImportError:
    subprocess.run('pip install mysql-connector-python', shell=True)

# Database connection
connection = connect(
    host="localhost",
    user="root",  # Replace with your MySQL username
    password="Pa$$w0rd",  # Replace with your MySQL password
    database="netfloux"
)


# Function to get films based on category_id
def get_films_from_category(category_id):
    cursor = connection.cursor()
    query = "SELECT * FROM movies WHERE category_id = %s"
    cursor.execute(query, (category_id,))
    films_to_diplay = cursor.fetchall()
    cursor.close()
    return films_to_diplay


# Function to retrieve all categories
def get_categories():
    cursor = connection.cursor()
    query = "SELECT * FROM categories"
    cursor.execute(query)
    categories = cursor.fetchall()
    cursor.close()
    return categories


# Function to get information about a film by its id
def get_films_informations(id):
    cursor = connection.cursor()
    query = "SELECT * FROM movies WHERE id = %s"
    cursor.execute(query, (id,))
    film_infos = cursor.fetchone()
    cursor.close()
    return film_infos


# Function to get a category name by its id
def get_category_from_id(id):
    cursor = connection.cursor()
    query = "SELECT name FROM categories WHERE id = %s"
    cursor.execute(query, (id,))
    category_name = cursor.fetchone()
    cursor.close()
    return category_name

# Function to insert a comment and rating for a movie
def insert_comment_and_rating(movie_id, username, comment, rating):
    cursor = connection.cursor()
    query = """
    INSERT INTO commentaries (commentar,username, rate, movie_id)
    VALUES (%s, %s, %s, %s)
    """
    cursor.execute(query, (comment,username, rating, movie_id))
    connection.commit()
    cursor.close()

# Function to get the average rating of a movie
def get_average_rating(movie_id):
    cursor = connection.cursor()
    query = "SELECT AVG(rate) FROM commentaries WHERE movie_id = %s"
    cursor.execute(query, (movie_id,))
    average_rating = cursor.fetchone()[0]  # Fetch the result
    cursor.close()

    # If no ratings exist, return 0
    return average_rating if average_rating is not None else 0

# Function to get all comments for a specific movie
def get_comments_for_movie(movie_id):
    cursor = connection.cursor()
    query = "SELECT commentar, rate FROM commentaries WHERE movie_id = %s"
    cursor.execute(query, (movie_id,))
    comments = cursor.fetchall()
    cursor.close()
    return comments