from database import get_films_informations,get_category_from_id
from customtkinter import *
from PIL import Image, ImageTk

# Initialisation of the app
set_appearance_mode("dark")  # Modes: "System" (default), "Dark", "Light"
set_default_color_theme("./content/color_theme.json")


def film_showed(id):
    film_informations_list = get_films_informations(id)

    name = film_informations_list[1]
    category = get_category_from_id(film_informations_list[-1])[0]
    release_date = film_informations_list[6]
    duration = f"{str(film_informations_list[2])[0:1]}h{str(film_informations_list[2])[2:4]}"
    minimum_age = film_informations_list[4]
    streaming_website = film_informations_list[5]

    # Main window creation
    Windowfilm = CTk()
    Windowfilm.title(name)
    Windowfilm.iconbitmap('images/goat.ico')
    Windowfilm.geometry("400x200")

    # Film image
    #film_image = CTkImage(light_image=Image.open('./images/netflix_logo.png'), dark_image=Image.open('./images/netflix_logo.png'), size=(150, 150))

    # Label to show film's name
    name_label = CTkLabel(Windowfilm, text=name)
    #image_label = CTkLabel(Windowfilm, image=film_image, text="")
    category_label = CTkLabel(Windowfilm, text=f"Genre: {category}")
    release_date_label = CTkLabel(Windowfilm, text=f"Date de sortie: {release_date}")
    duration_label = CTkLabel(Windowfilm, text=f"Durée: {duration}")
    minimum_age_label = CTkLabel(Windowfilm, text=f"Age minimal : {minimum_age} ans")
    streaming_site_label = CTkLabel(Windowfilm, text=f"Plateforme de streaming: {streaming_website}")


    name_label.pack(pady=10,ANCHOR=CENTER)
    #image_label.pack(anchor=LEFT)
    category_label.pack()
    release_date_label.pack()
    duration_label.pack()
    minimum_age_label.pack()
    streaming_site_label.pack()

    
    # app start
    Windowfilm.mainloop()

