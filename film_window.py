from database import get_films_informations, get_category_from_id
from customtkinter import *
from PIL import Image

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
    description = ('\n'.join([(film_informations_list[7])[i:i+25] for i in range(0, len((film_informations_list[7])), 25)]))
    trailer_link = film_informations_list[8]

    # Main window creation
    windowfilm = CTk()
    windowfilm.title(name)
    windowfilm.iconbitmap('images/goat.ico')
    windowfilm.geometry("400x250")

    # Film image (non fonctionnel pour le moment)
    # film_image = CTkImage(light_image=Image.open('./images/fleche.png'), dark_image=Image.open('./images/fleche.png'), size=(50, 50))

    # (non fonctionnel pour le moment)
    # image_label = CTkLabel(windowfilm, image=film_image, text="")

    # Label for the film name
    name_label = CTkLabel(windowfilm, text=name, font=("Arial", 25))

    # Frame that will contain all the films informations except for the name
    infos = CTkFrame(windowfilm, bg_color="transparent", fg_color="transparent")
    category_label = CTkLabel(infos, text=f"Genre: {category}")
    release_date_label = CTkLabel(infos, text=f"Date de sortie: {release_date}")
    duration_label = CTkLabel(infos, text=f"Durée: {duration}")
    minimum_age_label = CTkLabel(infos, text=f"Age minimal : {minimum_age} ans")
    streaming_site_label = CTkLabel(infos, text=f"Plateforme de streaming: {streaming_website}")
    description_label = CTkLabel(infos, text=f"Description: {description}")
    trailer_link = CTkLabel(infos, text=f"Trailer : {trailer_link}")


    # Placement of all the elements in the window
    name_label.pack(pady=10)
    infos.pack()
    category_label.pack()
    release_date_label.pack()
    duration_label.pack()
    minimum_age_label.pack()
    streaming_site_label.pack()
    description_label.pack()
    trailer_link.pack()

    
    # app start
    windowfilm.mainloop()

