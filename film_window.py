from database import get_films_informations, get_category_from_id, insert_comment_and_rating,get_average_rating, get_comments_for_movie
from customtkinter import *
from customtkinter import CTkImage
from PIL import Image,ImageTk
import webview  # Ajoute un Webview pour afficher les vidéos YouTube
from tkinter import messagebox

# Initialisation de l'application
set_appearance_mode("dark")  # Modes: "System" (default), "Dark", "Light"
set_default_color_theme("./content/color_theme.json")

def submit_rating(movie_id, selected_rating, username, comment_box, rating_label, comment_label):
    # Retrieve the comment and the rating
    comment = comment_box.get("0.0", "end").strip()  # Get the comment text
    rating = selected_rating.get()
    username = username.get()
    if  username != "":
        # Insert the comment and rating into the database
        insert_comment_and_rating(movie_id, username, comment, rating)

        # Update the rating and comment labels
        rating_label.configure(text=f"Votre note: {rating} étoiles")
        comment_label.configure(text=f"Votre commentaire: {comment}" if comment else "Aucun commentaire laissé")
    else:
        messagebox.showerror("Erreur", "Veuillez entrer votre nom d'utilisateur")

def rate_film(movie_id):
    # Create a new window for rating
    rate_window = CTkToplevel()
    rate_window.title("Rate the Film")
    rate_window.iconbitmap('images/goat.ico')
    rate_window.geometry("400x500")

    #variable de texte pour le username
    username = StringVar()

    # Label to prompt user to rate the film
    rate_label = CTkLabel(rate_window, text="Veuillez évaluer le film:", font=("Arial", 18))
    rate_label.pack(pady=10)

    # Create a variable to store the selected rating
    selected_rating = IntVar(value=0)

    # Create radio buttons for rating from 1 to 5
    rating_frame = CTkFrame(rate_window, fg_color="transparent")
    rating_frame.pack()
    star_image = CTkImage(Image.open("./images/star.png").resize((20, 20)))  # Resize the image to 20x20 pixels
    selected_rating = IntVar()
    for i in range(1, 6):
        label_frame = CTkFrame(rating_frame, fg_color="transparent")
        label_frame.pack(side=LEFT)

        rating_button = CTkButton(label_frame, fg_color="transparent", text="", border_width=0, image=star_image, width=20, height=20, command=lambda value=i: selected_rating.set(value))
        rating_button.pack(anchor=CENTER)
    E_username = CTkEntry(rate_window,width=250,height=10, placeholder_text="Username", textvariable=username).pack()
    comment_box = CTkTextbox(rate_window, width=300, height=100)
    comment_box.pack(pady=5)

    # Label to display the selected rating and comment
    rating_label = CTkLabel(rate_window, text="", font=("Arial", 14))
    rating_label.pack(pady=5)

    comment_display_label = CTkLabel(rate_window, text="", font=("Arial", 14))
    comment_display_label.pack()

    # Submit button to submit the rating and comment
    submit_button = CTkButton(rate_window, text="Soumettre", command=lambda: submit_rating(movie_id, selected_rating, username, comment_box, rating_label, comment_display_label))
    submit_button.pack()


def show_comments_window(movie_id):
    # Create a new window to display comments
    comments_window = CTkToplevel()
    comments_window.title("Comments")
    comments_window.geometry("450x500")

    # Scrollable frame for the comments
    scrollable_frame = CTkScrollableFrame(comments_window, width=400, height=450,bg_color="transparent", fg_color="transparent")
    scrollable_frame.pack(pady=10, padx=10, fill="both", expand=True)

    # Retrieve comments from the database
    comments = get_comments_for_movie(movie_id)

    # Check if there are comments
    if comments:
        for username, comment, rate in comments:
            # Frame for each comment with padding around it
            comment_frame = CTkFrame(scrollable_frame, fg_color="gray25", corner_radius=10)
            comment_frame.pack(pady=10, padx=15, fill="x", anchor="w")

            # Display the username in bold
            username_label = CTkLabel(
                comment_frame, text=f"👤 {username}", font=("Arial", 12, "bold"), anchor="w", text_color="cyan"
            )
            username_label.pack(anchor="w", padx=10, pady=(8, 2))

            # Display the comment text
            comment_label = CTkLabel(
                comment_frame, text=f"📝 {comment}", font=("Arial", 11), anchor="w", wraplength=380
            )
            comment_label.pack(anchor="w", padx=10, pady=(2, 5))

            # Display the rating with a star icon
            rating_label = CTkLabel(
                comment_frame, text=f"⭐ Rating: {rate} / 5", font=("Arial", 11, "bold"), anchor="w", text_color="gold"
            )
            rating_label.pack(anchor="w", padx=10, pady=(0, 8))
    else:
        # Message if no comments are available
        no_comments_label = CTkLabel(scrollable_frame, text="No comments yet.", font=("Arial", 13))
        no_comments_label.pack(pady=20)


def open_video(name,url):
    # Open a web interface in youtube to watch the trailer
    webview.create_window(name, url)
    webview.start()


def film_showed(id):
    # Retrieve the film's information from the database
    film_informations_list = get_films_informations(id)

    # Extract film details
    name = film_informations_list[1]
    category = get_category_from_id(film_informations_list[-1])[0]
    release_date = film_informations_list[6]
    duration = f"{str(film_informations_list[2])[0:1]}h{str(film_informations_list[2])[2:4]}"
    minimum_age = film_informations_list[4]
    streaming_website = film_informations_list[5]
    description = '\n'.join([(film_informations_list[7])[i:i + 25] for i in range(0, len((film_informations_list[7])), 25)])
    trailer_link = film_informations_list[8]

    # Get the average rating for the film
    average_rating = get_average_rating(id)

    # Main window
    windowfilm = CTk()
    windowfilm.title(name)
    windowfilm.iconbitmap('images/goat.ico')
    windowfilm.geometry("800x450")

    # Display film information
    name_label = CTkLabel(windowfilm, text=name, font=("Arial", 25))

    # Frame containing the film's information
    infos = CTkFrame(windowfilm, fg_color="transparent")
    category_label = CTkLabel(infos, text=f"Genre: {category}")
    release_date_label = CTkLabel(infos, text=f"Release date: {release_date}")
    duration_label = CTkLabel(infos, text=f"Duration: {duration}")
    minimum_age_label = CTkLabel(infos, text=f"Minimum age: {minimum_age} years")
    streaming_site_label = CTkLabel(infos, text=f"Streaming platform: {streaming_website}")
    description_label = CTkLabel(infos, text=f"Description: {description}")

    # Average rating label
    if average_rating is not None:
        average_rating_label = CTkLabel(infos, text=f"Average rating: {average_rating:.1f} stars")
    else:
        average_rating_label = CTkLabel(infos, text="No ratings yet")

    # Arrange information labels
    name_label.pack(pady=10)
    infos.pack(pady=5)
    category_label.pack()
    release_date_label.pack()
    duration_label.pack()
    minimum_age_label.pack()
    streaming_site_label.pack()
    description_label.pack()
    average_rating_label.pack(pady=5) 

    # Trailer button
    if trailer_link:
        play_button = CTkButton(windowfilm, text="Watch the trailer", command=lambda: open_video(name, trailer_link))
        play_button.pack(pady=20)

    # Rate button
    rate_button = CTkButton(windowfilm, text="Rate", command=lambda: rate_film(id))
    rate_button.pack(pady=10)
    # Comments button
    comments_button = CTkButton(windowfilm, text="Comments", command=lambda: show_comments_window(id))
    comments_button.pack(pady=10)
    # App start
    windowfilm.mainloop()
