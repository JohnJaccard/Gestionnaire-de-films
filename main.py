from customtkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

# Initialisation de l'application
set_appearance_mode("dark")  # Modes: "System" (default), "Dark", "Light"
set_default_color_theme("blue")  # Themes: "blue" (default), "dark-blue", "green"

# Création de la fenêtre principale
root = CTk()
root.title("App's Title")
root.geometry("800x700")

# Charger l'image du logo Netflix
try:
    image = Image.open("./images/netflix_logo.png")
    image = image.resize((150, 150))
    netflix_logo = ImageTk.PhotoImage(image)
except Exception as e:
    print("Erreur lors du chargement de l'image:", e)
    netflix_logo = None


# Fonction pour afficher un message avec la catégorie sélectionnée
def show_categories(category_id):
    if category_id == 1:  # Si "Films" est sélectionné
        display_film_buttons()
    elif category_id == 2:  # Si "Séries TV" est sélectionné
        messagebox.showinfo("Error", "Bientôt disponible")


# Fonction pour afficher les boutons des films depuis le bas
def display_film_buttons():
    # Cache les boutons "Films" et "Séries TV"
    button_films.place_forget()
    button_series.place_forget()

    # Afficher le bouton "Back"
    back_button.place(relx=0.9, rely=0.1, anchor=CENTER)

    # Affiche les boutons pour les films depuis le bas
    global film_buttons
    film_buttons = []
    y_position = 0.95
    for film_id, film_name in films.items():
        film_button = CTkButton(root, text=film_name, width=200, height=40,
                                command=lambda fid=film_id: messagebox.showinfo("Film sélectionné",
                                                                                f"Vous avez sélectionné : {films[fid]} (ID: {fid})"))
        film_button.place(relx=0.5, rely=y_position, anchor=CENTER)
        film_buttons.append(film_button)
        y_position -= 0.1  # Place chaque bouton un peu plus haut que le précédent


# Fonction pour revenir à l'écran principal
def back_to_main_menu():
    # Détruit les boutons des films
    for btn in film_buttons:
        btn.destroy()

    # Cache le bouton "Back"
    back_button.place_forget()

    # Remet en place les boutons "Films" et "Séries TV"
    button_films.place(relx=0.25, rely=0.6, anchor=CENTER)
    button_series.place(relx=0.75, rely=0.6, anchor=CENTER)


# Catégories de début
categories = {
    1: "Films",
    2: "Séries TV"
}

# Liste des films
films = {
    1: "Action",
    2: "Horreur",
    3: "Comédies",
    4: "Science-fiction",
    5: "Romances"
}

# Liste pour stocker les boutons des films
film_buttons = []

# Ajout du logo Netflix au centre
if netflix_logo:
    logo_label = CTkLabel(root, image=netflix_logo, text="")
    logo_label.place(relx=0.5, rely=0.4, anchor=CENTER)

# Création des boutons pour les catégories "Films" et "Séries TV"
button_width = 100
button_height = 40

# Bouton pour "Films" (à gauche)
button_films = CTkButton(root, text=categories[1], width=button_width, height=button_height,
                         command=lambda: show_categories(1))
button_films.place(relx=0.25, rely=0.6, anchor=CENTER)

# Bouton pour "Séries TV" (à droite)
button_series = CTkButton(root, text=categories[2], width=button_width, height=button_height,
                          command=lambda: show_categories(2))
button_series.place(relx=0.75, rely=0.6, anchor=CENTER)

# Création du bouton "Back" (invisible au début)
back_button = CTkButton(root, text="Back", width=80, height=30, command=back_to_main_menu)

# Lancement de l'application
root.mainloop()
