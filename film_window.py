from database import get_films_informations
from customtkinter import *

# Initialisation of the app
set_appearance_mode("dark")  # Modes: "System" (default), "Dark", "Light"
set_default_color_theme("./content/color_theme.json")


def film_showed(id):
    film_name = get_films_informations(id)

    # Main window creation
    Windowfilm = CTk()
    Windowfilm.title("Prendre le nom du film via l'ID")
    Windowfilm.iconbitmap('images/goat.ico')
    Windowfilm.geometry("400x200")

    # Label to show film's name
    film_name_label = CTkLabel(Windowfilm, text=film_name)
    film_name_label.pack(pady=10)
    
    # app start
    Windowfilm.mainloop()

