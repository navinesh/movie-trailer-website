import media
import fresh_tomatoes

# movie instances
titanic = media.Movie("Titanic",
                      "James Cameron",
                      "Leonardo DiCaprio, Kate Winslet, Billy Zane",
                      "http://goo.gl/TtkWP1",
                      "https://www.youtube.com/watch?v=2e-eXJ6HgkQ")

as_good_as_it_gets = media.Movie("As Good As It Gets",
                                 "James L. Brooks",
                                 "Jack Nicholson, Helen Hunt, Greg Kinnear",
                                 "http://goo.gl/sRVhT5",
                                 "https://www.youtube.com/watch?v=rrRl2QQKkI8")

the_wolverine = media.Movie("The Wolverine",
                            "James Mangold",
                            "Hugh Jackman, Hiroyuki Sanada, Tao Okamoto",
                            "http://goo.gl/r0IWUq",
                            "https://www.youtube.com/watch?v=th1NTVIhUQU")

inception = media.Movie("Inception",
                        "Christopher Nolan",
                        "Leonardo DiCaprio, Ken Watanabe, \
                        Joseph Gordon-Levitt",
                        "https://goo.gl/xgzhky",
                        "https://www.youtube.com/watch?v=8hP9D6kZseM")

the_avengers = media.Movie("The Avengers",
                           "Joss Whedon",
                           "Robert Downey Jr., Chris Evans, Mark Ruffalo, \
                           Chris Hemsworth, Scarlett Johansson, Jeremy Renner",
                           "http://goo.gl/dAvzJg",
                           "https://www.youtube.com/watch?v=eOrNdBpGMv8")

the_hangover = media.Movie("The Hangover",
                           "Todd Phillips",
                           "Bradley Cooper, Ed Helms, Zach Galifianakis",
                           "http://goo.gl/sz9K6H",
                           "https://www.youtube.com/watch?v=vhFVZsk3XEs")

# list of movies
movies = [titanic, as_good_as_it_gets, the_wolverine, inception,
          the_avengers, the_hangover]

# pass list of movies to build html page to display website
fresh_tomatoes.open_movies_page(movies)
