import webbrowser

class Movie():
    """This is a movie object. It has three private attributes and you are welcome to use 'dir(Movie)' to check them out.
       Also, it has a method named 'show_trailer', which basically opens the trailer url for you in your browser."""

    def __init__(self, title, poster_image, trailer_youtube):
        self.title = title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
