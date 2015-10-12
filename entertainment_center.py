import media
import fresh_tomatoes

#movie instances
titanic = media.Movie("Titanic",
                        "James Cameron",
                        "Leonardo DiCaprio, Kate Winslet, Billy Zane",
                        "http://ecx.images-amazon.com/images/I/91rZp5zs8kL._SL1500_.jpg",
                        "https://www.youtube.com/watch?v=2e-eXJ6HgkQ")
as_good_as_it_gets = media.Movie("As Good As It Gets",
                                    "James L. Brooks",
                                    "Jack Nicholson, Helen Hunt, Greg Kinnear",
                                    "http://images.moviepostershop.com/as-good-as-it-gets-movie-poster-1997-1020213557.jpg",
                                    "https://www.youtube.com/watch?v=rrRl2QQKkI8")
the_wolverine = media.Movie("The Wolverine",
                            "James Mangold",
                            "Hugh Jackman, Hiroyuki Sanada, Tao Okamoto",
                            "http://www.iceposter.com/thumbs/MOV_3933d52b_b.jpg",
                            "https://www.youtube.com/watch?v=th1NTVIhUQU")
inception = media.Movie("Inception",
                        "Christopher Nolan",
                        "Leonardo DiCaprio, Ken Watanabe, Joseph Gordon-Levitt",
                        "https://trailers.apple.com/trailers/wb/inception/images/poster-large.jpg?lastmod=1",
                        "https://www.youtube.com/watch?v=8hP9D6kZseM")
the_avengers = media.Movie("The Avengers",
                            "Joss Whedon",
                            "Robert Downey Jr., Chris Evans, Mark Ruffalo, Chris Hemsworth, Scarlett Johansson, Jeremy Renner",
                            "http://palarisme.ro/images/filme/marvel/sd.jpg",
                            "https://www.youtube.com/watch?v=eOrNdBpGMv8")
the_hangover = media.Movie("The Hangover",
                            "Todd Phillips",
                            "Bradley Cooper, Ed Helms, Zach Galifianakis",
                            "http://www.coverwhiz.com/content/The-Hangover-Part-1.jpg",
                            "https://www.youtube.com/watch?v=vhFVZsk3XEs")

#list of movies
movies = [titanic, as_good_as_it_gets, the_wolverine, inception, the_avengers, the_hangover]

#pass list of movies to build html page to display website
fresh_tomatoes.open_movies_page(movies)
