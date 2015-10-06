import movie
import fresh_tomatoes

titanic = movie.Movie("Titanic", "http://ecx.images-amazon.com/images/I/91rZp5zs8kL._SL1500_.jpg", "https://www.youtube.com/watch?v=2e-eXJ6HgkQ")
as_good_as_it_gets = movie.Movie("As Good As It Gets", "http://images.moviepostershop.com/as-good-as-it-gets-movie-poster-1997-1020213557.jpg", "https://www.youtube.com/watch?v=rrRl2QQKkI8")
the_wolverine = movie.Movie("The Wolverine", "http://www.iceposter.com/thumbs/MOV_3933d52b_b.jpg", "https://www.youtube.com/watch?v=th1NTVIhUQU")
inception = movie.Movie("Inception", "https://trailers.apple.com/trailers/wb/inception/images/poster-large.jpg?lastmod=1", "https://www.youtube.com/watch?v=8hP9D6kZseM")
the_avengers = movie.Movie("The Avengers", "http://palarisme.ro/images/filme/marvel/sd.jpg", "https://www.youtube.com/watch?v=eOrNdBpGMv8")
interstellar = movie.Movie("Interstellar", "http://i.imgur.com/7Du30vM.jpg", "https://www.youtube.com/watch?v=zSWdZVtXT7E")
the_hangover = movie.Movie("The Hangover", "http://www.coverwhiz.com/content/The-Hangover-Part-1.jpg", "https://www.youtube.com/watch?v=vhFVZsk3XEs")
transformers = movie.Movie("Transformers", "http://ecx.images-amazon.com/images/I/51xbz6iJJ9L.jpg", "https://www.youtube.com/watch?v=UxI_JI6chas")
king_kong = movie.Movie("King Kong", "http://www.gstatic.com/tv/thumb/movieposters/90705/p90705_p_v7_aa.jpg", "https://www.youtube.com/watch?v=AYaTCPbYGdk")

movies = [titanic, as_good_as_it_gets, the_wolverine, inception, the_avengers, interstellar, the_hangover, transformers, king_kong]

fresh_tomatoes.open_movies_page(movies)
