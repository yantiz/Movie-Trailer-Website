import class_definition as cd
import fresh_tomatoes as ft

# Create three instances of Movie objects, with each of which contains information about a distinct movie.
toy_story = cd.Movie("Toy Story", "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg", "https://www.youtube.com/watch?v=vwyZH85NQC4")
interstellar = cd.Movie("Interstellar", "https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg", "https://www.youtube.com/watch?v=0vxOhd4qlnA") 
warcraft = cd.Movie("Warcraft", "https://upload.wikimedia.org/wikipedia/en/5/56/Warcraft_Teaser_Poster.jpg", "https://www.youtube.com/watch?v=65AjY_nRdqE")

# Put movies into a list and pass that list as an argument into the function 'open_movies_page' in order to generate the website.
movies = [toy_story, interstellar, warcraft]
ft.open_movies_page(movies)
