from customtkinter import *
from tkinter import messagebox

# Initialisation de l'application
set_appearance_mode("dark")  # Modes: "System" (default), "Dark", "Light"
set_default_color_theme("blue")  # Themes: "blue" (default), "dark-blue", "green"

# Création de la fenêtre principale
root = CTk()
root.title("Liste de Films")
root.geometry("400x500")

# Fonction pour afficher un message avec l'ID du film sélectionné
def show_film_info(film_id):
    film_name = films[film_id]
    messagebox.showinfo("Film sélectionné", f"Vous avez sélectionné : {film_name} (ID: {film_id})")

# Liste des films avec des IDs
films = {
    1: "Action",
    2: "Horreur",
    3: "Comédies",
    4: "Science-fiction",
    5: "Romances"
}

# Création de boutons pour chaque film dans la liste
for film_id, film_name in films.items():
    button = CTkButton(root, text=film_name, command=lambda fid=film_id: show_film_info(fid))
    button.pack(pady=10, padx=20, fill="x")

# Lancement de l'application
root.mainloop()
