class Movie():
    """Class to create instances of movies"""
    def __init__(self, movie_title, movie_director, movie_starring,
                 poster_image_url, trailer_youtube_url):
        """Inits Movie class with movie variables"""
        self.title = movie_title
        self.director = movie_director
        self.starring = movie_starring
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
