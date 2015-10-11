class Movie():
    """Movie class to create movie instances"""
    def __init__(self, movie_title, movie_director, movie_starring, poster_image_url, trailer_youtube_url):
        self.title = movie_title
        self.director = movie_director
        self.starring = movie_starring
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
