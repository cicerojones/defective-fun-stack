import media
import fresh_tomatoes

goy_story = media.Movie("Goy Story",
                        "A story of a goy and his toys...that come to kill him",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
                        )

goys_dont_cry = media.Movie("Goys Don't Cry",
                        "A story of a goy and his toys...that come to kill him",
                        "https://upload.wikimedia.org/wikipedia/en/3/3b/Boys_Don%27t_Cry_movie.jpg",
                        "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
                        )

goy_luck_club = media.Movie("The Goy Luck Club",
                        "A story of a goy and his toys...that come to kill him",
                        "https://upload.wikimedia.org/wikipedia/en/1/19/The_Joy_Luck_Club_%28film%29.jpg",
                        "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
                        )

goy = media.Movie("Goy",
                        "A story of a goy and his toys...that come to kill him",
                        "http://www.eonline.com/eol_images/Entire_Site/2015717/rs_634x939-150817124543-634-joy-jennifer-lawrence-Onesheet.jpg",
                        "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
                        )

goyz_n_the_hood = media.Movie("Goyz n the Hood",
                        "A story of a goy and his toys...that come to kill him",
                        "https://upload.wikimedia.org/wikipedia/en/c/c3/Boyz_n_the_hood_poster.jpg",
                        "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
                        )

babes_in_goyland = media.Movie("Babes in Goyland",
                        "A story of a goy and his toys...that come to kill him",
                        "https://upload.wikimedia.org/wikipedia/en/a/a7/L%26H_Babes_in_Toyland_1934.jpg",
                        "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
                        )


movies = [ goy_story, goys_dont_cry, goy_luck_club, goy, goyz_n_the_hood, babes_in_goyland ]
fresh_tomatoes.open_movies_page(movies)
