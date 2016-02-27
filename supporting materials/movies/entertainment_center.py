import media
import fresh_tomatoes

# create a bunch of fake movie titles based on real movies
# oh, and mix up the urls, just for more fun
goy_story = media.Movie("Goy Story",
                        "A story of a goy and his toys...that come to kill him",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=aOarssJWHhI"
                        )

goys_dont_cry = media.Movie("Goys Don't Cry",
                            "A story of a goy and his toys...that come to kill him",
                            "https://upload.wikimedia.org/wikipedia/en/3/3b/Boys_Don%27t_Cry_movie.jpg",
                            "https://www.youtube.com/watch?v=KYz2wyBy3kc"
                            )

goy_luck_club = media.Movie("The Goy Luck Club",
                            "A story of a goy and his toys...that come to kill him",
                            "https://upload.wikimedia.org/wikipedia/en/1/19/The_Joy_Luck_Club_%28film%29.jpg",
                            "https://www.youtube.com/watch?v=SN4MLMHET7w"
                            )

goy = media.Movie("Goy",
                  "A story of a goy and his toys...that come to kill him",
                  "http://www.eonline.com/eol_images/Entire_Site/2015717/rs_634x939-150817124543-634-joy-jennifer-lawrence-Onesheet.jpg",
                  "https://www.youtube.com/watch?v=0nYDMp1LdT8"
                  )

goyz_n_the_hood = media.Movie("Goyz n the Hood",
                              "A story of a goy and his toys...that come to kill him",
                              "https://upload.wikimedia.org/wikipedia/en/c/c3/Boyz_n_the_hood_poster.jpg",
                              "https://www.youtube.com/watch?v=HcfGmolIi1Q"
                              )


babes_in_goyland = media.Movie("Babes in Goyland",
                               "A story of a goy and his toys...that come to kill him",
                               "https://upload.wikimedia.org/wikipedia/en/a/a7/L%26H_Babes_in_Toyland_1934.jpg",
                               "https://www.youtube.com/watch?v=AE4BdijGtu4"
                               )


# Create list of above Movie objects
movies = [goy_story, goys_dont_cry,
          goy_luck_club, goy,
          goyz_n_the_hood, babes_in_goyland
          ]

# call function with the above list of movies to render a page of HTML
fresh_tomatoes.open_movies_page(movies)
