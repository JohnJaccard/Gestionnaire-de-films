from database import get_films_informations,get_category_from_id
from customtkinter import *
from PIL import Image, ImageTk

# Initialisation of the app
set_appearance_mode("dark")  # Modes: "System" (default), "Dark", "Light"
set_default_color_theme("./content/color_theme.json")


def film_showed(id):
    # Get all the informations from the database in a list obtained by the function get_films_informations
    film_informations_list = get_films_informations(id)

    # Separate each element from the list (and a specific format for the duration)
    name = film_informations_list[1]
    category = get_category_from_id(film_informations_list[-1])[0]
    release_date = film_informations_list[6]
    duration = f"{str(film_informations_list[2])[0:1]}h{str(film_informations_list[2])[2:4]}"
    minimum_age = film_informations_list[4]
    streaming_website = film_informations_list[5]

    # Main window creation
    windowfilm = CTk()
    windowfilm.title(name)
    windowfilm.iconbitmap('images/goat.ico')
    windowfilm.geometry("400x200")

    # Film image (non fonctionnel pour le moment)
    #film_image = CTkImage(light_image=Image.open('./images/netflix_logo.png'), dark_image=Image.open('./images/netflix_logo.png'), size=(150, 150))


    # (non fonctionnel pour le moment)
    #image_label = CTkLabel(windowfilm, image=film_image, text="")

    # Label for each film's element
    name_label = CTkLabel(windowfilm, text=name)
    category_label = CTkLabel(windowfilm, text=f"Genre: {category}")
    release_date_label = CTkLabel(windowfilm, text=f"Date de sortie: {release_date}")
    duration_label = CTkLabel(windowfilm, text=f"Durée: {duration}")
    minimum_age_label = CTkLabel(windowfilm, text=f"Age minimal : {minimum_age} ans")
    streaming_site_label = CTkLabel(windowfilm, text=f"Plateforme de streaming: {streaming_website}")


    # Placement of all the elements in the window
    name_label.pack(pady=10,ANCHOR=CENTER)
    #image_label.pack(anchor=LEFT)
    category_label.pack()
    release_date_label.pack()
    duration_label.pack()
    minimum_age_label.pack()
    streaming_site_label.pack()

    
    # app start
    windowfilm.mainloop()

