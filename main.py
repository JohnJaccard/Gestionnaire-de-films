import customtkinter as ctk
from tkinter import messagebox

# Initialisation de l'application
ctk.set_appearance_mode("dark")  # Modes: "System" (default), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (default), "dark-blue", "green"

# Création de la fenêtre principale
root = ctk.CTk()
root.title("Liste de Films")
root.geometry("400x500")

# Fonction pour afficher un message avec l'ID du film sélectionné
def show_film_info(film_id):
    film_name = films[film_id]
    messagebox.showinfo("Film sélectionné", f"Vous avez sélectionné : {film_name} (ID: {film_id})")

# Liste des films avec des IDs
films = {
    1: "Inception",
    2: "The Matrix",
    3: "Interstellar",
    4: "The Dark Knight",
    5: "Pulp Fiction"
}

# Création de boutons pour chaque film dans la liste
for film_id, film_name in films.items():
    button = ctk.CTkButton(root, text=film_name, command=lambda fid=film_id: show_film_info(fid))
    button.pack(pady=10, padx=20, fill="x")

# Lancement de l'application
root.mainloop()
