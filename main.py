from customtkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from film_window import film_showed
from database import get_films_from_category,get_categories


# Initialisation de l'application
set_appearance_mode("dark")  # Modes: "System" (default), "Dark", "Light"
set_default_color_theme("./content/color_theme.json")

# Création de la fenêtre principale
root = CTk()
root.title("Netfloux")
root.iconbitmap('images/goat.ico')
root.geometry("800x700")


# Variables
# paramètres des boutons de l'accueil
button_width = 100
button_height = 60
# paramètres des boutons des films
film_btn_height = 100
film_btn_width = 150
# variables pour le tri par catégorie
f_cat = 0

#images
logo = CTkImage(light_image=Image.open('./images/netflix_logo.png'), dark_image=Image.open('./images/netflix_logo.png'), size=(150, 150))  # WidthxHeight
fleche = CTkImage(light_image=Image.open('./images/fleche.png'), dark_image=Image.open('./images/fleche.png'), size=(50, 50))

# Catégories de début
categories = {
    1: "Films",
    2: "Séries TV"
}

# Liste pour stocker les boutons des films
film_buttons = []
films_btn = []

# fonctions
def display_films_from_category(category_id):
    global films_btn
    # liste des films à afficher
    films_to_diplay = []
    # liste des boutons des films à afficher
    films_btn =[]
    # base du grid
    grid_row = 1
    grid_column = 1

    films_to_diplay = get_films_from_category(category_id)

    # vérif si il y a des films à afficher
    if len(films_to_diplay) > 0:
        films_categories_frame.place_forget()
        for btn in film_buttons:
            btn.destroy()

        films_frame.place(relx=0.55, rely=0.7, anchor=CENTER)
        # Affiche le bouton "Back"Afficher les boutons des films de la catégorie sélectionnée
        for film in films_to_diplay:
            film_btn = CTkButton(films_frame, text=('\n'.join([(film[1])[i:i+10] for i in range(0, len((film[1])), 10)])),height=film_btn_height, width=film_btn_width,command=lambda filmid=film[0]:film_showed(filmid) ,corner_radius=20, fg_color=["#92140C", "#92140C"])
            # Positionner le bouton dans la grille
            film_btn.grid(row=grid_row, column=grid_column, padx=10, pady=10)
            films_btn.append(film_btn)
            grid_column += 1
            if grid_column > 2:
                grid_row += 1
                grid_column = 1

# Fonction pour revenir à l'écran principal
def back_to_main_menu():
    global films_btn
    # Détruit les boutons des films
    for btn in film_buttons:
        btn.destroy()

    for btn in films_btn:
        btn.destroy()
    films_categories_frame.place_forget()
    films_frame.place_forget()

    # Cache le bouton "Back"
    back_button.place_forget()

    # Remet en place les boutons "Films" et "Séries TV"
    button_films.place(relx=0.25, rely=0.6, anchor=CENTER)
    button_series.place(relx=0.75, rely=0.6, anchor=CENTER)

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
    # placement de la frame pour avoir les éléments scrollables
    films_categories_frame.place(relx=0.353,rely=0.42)
    #récup info des catégories selectionné
    categories = get_categories()
    for category in categories:
        film_button = CTkButton(films_categories_frame, text=category[1], width=200, height=40,
                                command=lambda fid=category[0]: display_films_from_category(fid))
        film_button.pack(pady=10)
        film_buttons.append(film_button)

# Fonction pour afficher un message avec la catégorie sélectionnée
def show_categories(category_id):
    if category_id == 1:  # Si "Films" est sélectionné
        display_film_buttons()
    elif category_id == 2:  # Si "Séries TV" est sélectionné
        messagebox.showinfo("Error", "Bientôt disponible")


# Création des widgets
# frames
films_categories_frame = CTkScrollableFrame(root, fg_color="#272529", height=250, corner_radius=20)
films_frame = CTkScrollableFrame(root, bg_color="transparent", fg_color="transparent",width=400,height=350)

# labels
logo_label = CTkLabel(root, image=logo, text="")

# boutons
# Bouton pour "Films" (à gauche)
button_films = CTkButton(root, text=categories[1], width=button_width, height=button_height,
                         command=lambda: show_categories(1))

# Création du bouton "Back" (invisible au début)
back_button = CTkButton(root, fg_color="transparent",border_width=0, text="", image=fleche, width=80, height=30, command=back_to_main_menu)

# Bouton pour "Séries TV" (à droite)
button_series = CTkButton(root, text=categories[2], width=button_width, height=button_height,
                          command=lambda: show_categories(2))


#placement des objets
logo_label.place(relx=0.5, rely=0.3, anchor=CENTER)
button_films.place(relx=0.25, rely=0.6, anchor=CENTER)
button_series.place(relx=0.75, rely=0.6, anchor=CENTER)


# Lancement de l'application
root.mainloop()
