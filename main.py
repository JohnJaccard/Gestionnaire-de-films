from tkinter import messagebox
from film_window import film_showed
from database import get_films_from_category, get_categories
import subprocess
# Try to import the packages and if it fails, install it
# Customtkinter
try:
    from customtkinter import *
    print('customtkinter already installed')
except:
    subprocess.run('pip install customtkinter', shell=True)
    from customtkinter import *
# Pillow
try:
    from PIL import Image
    print('pillow already installed')
except:
    subprocess.run('pip install pillow', shell=True)
    from PIL import Image

# Initialisation of the app
set_appearance_mode("dark")  # Modes: "System" (default), "Dark", "Light"
set_default_color_theme("./content/color_theme.json")

# Creation of the main window
root = CTk()
root.title("Netfloux")
root.iconbitmap('images/goat.ico')
root.geometry("800x700")


# Variables
# Sizes of home buttons
button_width = 100
button_height = 60
# Sizes of the films buttons
film_btn_height = 100
film_btn_width = 150
# Variables for sorting the categories
f_cat = 0

# Images
logo = CTkImage(light_image=Image.open('./images/netflix_logo.png'), dark_image=Image.open('./images/netflix_logo.png'), size=(150, 150))
fleche = CTkImage(light_image=Image.open('./images/fleche.png'), dark_image=Image.open('./images/fleche.png'), size=(50, 50))

# Choose between films and series
categories = {
    1: "Films",
    2: "Séries TV"
}

# Lists that will contain films buttons
categories_buttons = []
films_btn = []

# Functions
def display_films_from_category(category_id):
    global films_btn
    # buttons lists
    films_btn = []
    # Grid parameters
    grid_row = 1
    grid_column = 1

    # Use a database connection to obtain films from a category that was clicked
    films_to_diplay = get_films_from_category(category_id)

    # Check if there's films in the category, if not it doesn't do anything
    if len(films_to_diplay) > 0:
        # Unplace the categories frame to make the categories buttons dissappear
        films_categories_frame.place_forget()
        for btn in categories_buttons:
            btn.destroy()

        # Place the films frame
        films_frame.place(relx=0.55, rely=0.7, anchor=CENTER)
        # Display all the films in a grid
        for film in films_to_diplay:
            film_btn = CTkButton(films_frame, text=('\n'.join([(film[1])[i:i+10] for i in range(0, len((film[1])), 10)])),height=film_btn_height, width=film_btn_width,command=lambda filmid=film[0]:film_showed(filmid),corner_radius=20)
            # Place the buttons in the grid
            film_btn.grid(row=grid_row, column=grid_column, padx=10, pady=10)
            films_btn.append(film_btn)
            # Make the grid of films witdh at 2 maximum
            grid_column += 1
            if grid_column > 2:
                grid_row += 1
                grid_column = 1

# Function for the "back" button to go the home page
def back_to_main_menu():
    global films_btn
    # Destroy categories buttons and frame
    for btn in categories_buttons:
        btn.destroy()
    films_categories_frame.place_forget()
    # Destroy films buttons and frame
    for btn in films_btn:
        btn.destroy()
    films_frame.place_forget()

    # Unplace the back button
    back_button.place_forget()

    # Place again the home buttons to choose between films and series
    button_films.place(relx=0.25, rely=0.6, anchor=CENTER)
    button_series.place(relx=0.75, rely=0.6, anchor=CENTER)

# Function that will display all the categories
def display_categories_buttons():
    global categories_buttons
    # Unplace the films and series buttons
    button_films.place_forget()
    button_series.place_forget()

    # Place the Back button
    back_button.place(relx=0.9, rely=0.1, anchor=CENTER)

    # Categories list
    categories_buttons = []
    # Placement for the category's frame
    films_categories_frame.place(relx=0.353,rely=0.42)
    # Take all the categories from the database
    categories = get_categories()
    # Display the categories as buttons in the frame
    for category in categories:
        film_button = CTkButton(films_categories_frame, text=category[1], width=200, height=40,
                                command=lambda fid=category[0]: display_films_from_category(fid))
        film_button.pack(pady=10)
        categories_buttons.append(film_button)

# Function to differentiate the films and the series
def show_categories(category_id):
    if category_id == 1:  # If films is selected
        display_categories_buttons()
    elif category_id == 2:  # if series is selected
        messagebox.showinfo("Error", "Bientôt disponible")


# Widgets creation
# Frames
films_categories_frame = CTkScrollableFrame(root, fg_color="#272529", height=250, corner_radius=20)
films_frame = CTkScrollableFrame(root, bg_color="transparent", fg_color="transparent",width=400,height=350)

# Labels
logo_label = CTkLabel(root, image=logo, text="")

# Buttons
# Button films
button_films = CTkButton(root, text=categories[1], width=button_width, height=button_height,
                         command=lambda: show_categories(1))

# Back button
back_button = CTkButton(root, fg_color="transparent",border_width=0, text="", image=fleche, width=80, height=30, command=back_to_main_menu)

# Button series
button_series = CTkButton(root, text=categories[2], width=button_width, height=button_height,
                          command=lambda: show_categories(2))


# Placement
logo_label.place(relx=0.5, rely=0.3, anchor=CENTER)
button_films.place(relx=0.25, rely=0.6, anchor=CENTER)
button_series.place(relx=0.75, rely=0.6, anchor=CENTER)


# App start
root.mainloop()
