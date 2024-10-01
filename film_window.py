from database import get_films_informations, get_category_from_id, insert_comment_and_rating
from customtkinter import *
from PIL import Image
import os
import webview  # Ajoute un Webview pour afficher les vidéos YouTube

# Initialisation de l'application
set_appearance_mode("dark")  # Modes: "System" (default), "Dark", "Light"
set_default_color_theme("./content/color_theme.json")

def submit_rating(movie_id, selected_rating, comment_box, rating_label, comment_label):
    # Retrieve the comment and the rating
    comment = comment_box.get("0.0", "end").strip()  # Get the comment text
    rating = selected_rating.get()

    # Insert the comment and rating into the database
    insert_comment_and_rating(movie_id, comment, rating)

    # Update the rating and comment labels
    rating_label.configure(text=f"Votre note: {rating} étoiles")
    comment_label.configure(text=f"Votre commentaire: {comment}" if comment else "Aucun commentaire laissé")


def rate_film(movie_id):
    # Create a new window for rating
    rate_window = CTkToplevel()
    rate_window.title("Rate the Film")
    rate_window.iconbitmap('images/goat.ico')
    rate_window.geometry("400x500")

    # Label to prompt user to rate the film
    rate_label = CTkLabel(rate_window, text="Veuillez évaluer le film:", font=("Arial", 18))
    rate_label.pack(pady=10)

    # Create a variable to store the selected rating
    selected_rating = IntVar(value=0)

    # Create radio buttons for rating from 1 to 5
    for i in range(1, 6):
        rating_button = CTkRadioButton(rate_window, text=f"{i} étoile{'s' if i > 1 else ''}", variable=selected_rating, value=i)
        rating_button.pack()

    # Textbox to allow the user to input a comment
    comment_label = CTkLabel(rate_window, text="Laissez un commentaire:", font=("Arial", 16))
    comment_label.pack(pady=10)

    comment_box = CTkTextbox(rate_window, width=300, height=100)
    comment_box.pack(pady=5)

    # Label to display the selected rating and comment
    rating_label = CTkLabel(rate_window, text="", font=("Arial", 14))
    rating_label.pack(pady=5)

    comment_display_label = CTkLabel(rate_window, text="", font=("Arial", 14))
    comment_display_label.pack(pady=5)

    # Submit button to submit the rating and comment
    submit_button = CTkButton(rate_window, text="Soumettre", command=lambda: submit_rating(movie_id, selected_rating, comment_box, rating_label, comment_display_label))
    submit_button.pack(pady=10)


def open_video(name,url):
    # Open a web interface in youtube to watch the trailer
    webview.create_window(name, url)
    webview.start()

# Fonction pour afficher les informations du film et la bande-annonce
def film_showed(id):
    # Récupérer les informations du film depuis la base de données
    film_informations_list = get_films_informations(id)

    # Extraire les détails du film
    name = film_informations_list[1]
    category = get_category_from_id(film_informations_list[-1])[0]
    release_date = film_informations_list[6]
    duration = f"{str(film_informations_list[2])[0:1]}h{str(film_informations_list[2])[2:4]}"
    minimum_age = film_informations_list[4]
    streaming_website = film_informations_list[5]
    description = ('\n'.join([(film_informations_list[7])[i:i+25] for i in range(0, len((film_informations_list[7])), 25)]))
    trailer_link = film_informations_list[8]

    # Fenêtre principale
    windowfilm = CTk()
    windowfilm.title(name)
    windowfilm.iconbitmap('images/goat.ico')
    windowfilm.geometry("600x450")

    # Label pour le nom du film
    name_label = CTkLabel(windowfilm, text=name, font=("Arial", 25))

    # Frame contenant les informations du film
    infos = CTkFrame(windowfilm, fg_color="transparent")
    category_label = CTkLabel(infos, text=f"Genre: {category}")
    release_date_label = CTkLabel(infos, text=f"Date de sortie: {release_date}")
    duration_label = CTkLabel(infos, text=f"Durée: {duration}")
    minimum_age_label = CTkLabel(infos, text=f"Age minimal : {minimum_age} ans")
    streaming_site_label = CTkLabel(infos, text=f"Plateforme de streaming: {streaming_website}")
    description_label = CTkLabel(infos, text=f"Description: {description}")

    # Bouton to launch the video player (it's just a fake chrome)
    play_button = CTkButton(windowfilm, text="Regarder la bande-annonce", command=lambda: open_video(name,trailer_link))

    # "Rate" button
    rate_button = CTkButton(windowfilm, text="Noter", command=lambda: rate_film(id))


    # Placement des éléments dans la fenêtre
    name_label.pack(pady=10)
    infos.pack()
    category_label.pack()
    release_date_label.pack()
    duration_label.pack()
    minimum_age_label.pack()
    streaming_site_label.pack()
    description_label.pack()
    play_button.pack(pady=20)
    rate_button.pack(pady=20)  # Place the "Rate" button below the film information

    # App start
    windowfilm.mainloop()

