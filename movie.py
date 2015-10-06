import webbrowser

class Movie():
    """This is the Movie class to create movie instances"""
    def __init__(self, movie_title, poster_image_url, trailer_youtube_url):
        self.title = movie_title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url

        def show_trailer(self):
            webbrowser.open(self.trailer_youtube_url)
