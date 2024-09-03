from mysql.connector import *
from customtkinter import *
from PIL import Image, ImageTk

# Initialisation de l'application
set_appearance_mode("dark")  # Modes: "System" (default), "Dark", "Light"
set_default_color_theme("./content/color_theme.json")

connection = connect(
    host="localhost",
    user="root",   # Remplacez par votre utilisateur
    password="Pa$$w0rd", # Remplacez par votre mot de passe
    database="netfloux"
)

def film_showed(id):
    #récup info du film selectionné
    cursor = connection.cursor()
    # Requête pour récupérer le nom du film par ID
    query = "SELECT * FROM movies WHERE id = %s"
    cursor.execute(query, (id,))
    film_infos = cursor.fetchone()
    film_name = film_infos[1]
    # Fermeture de la connexion
    cursor.close()

    # Création de la fenêtre principale
    Windowfilm = CTk()
    Windowfilm.title("Prendre le nom du film via l'ID")
    Windowfilm.iconbitmap('images/goat.ico')
    Windowfilm.geometry("400x200")

    # Label pour afficher le nom du film
    film_name_label = CTkLabel(Windowfilm, text=film_name)
    film_name_label.pack(pady=10)
    
    # Lancement de l'application
    Windowfilm.mainloop()

# Exemple d'appel de la fonction avec une ID (à adapter)
film_showed(1)
