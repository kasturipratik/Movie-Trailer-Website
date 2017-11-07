# import classes form other python files
import media
import fresh_tomatoes

# create list of movies

# this is object or instances
toy_story = media.Movie("Toy Story",
                        "A strory of a boy and his toys that come to life",
                        "http://www.pixartalk.com/wp-content/uploads/2009/06/"
                        "ts1poster.jpg",
                        "https://www.youtube.com/watch?v=4KPTXpQehio")
# this is instances or object
wolf_story = media.Movie("Wolf warrior 2",
                         "Wolf warrior is about a secret army man in Africa",
                         "http://cdn.darkhorizons.com/wp-content/uploads/"
                         "2017/08/wolf-warriors-2-becomes-chinas-biggest"
                         "-film.jpg",
                         "https://www.youtube.com/watch?v=fkqGiPB2D8M")
# this is instances or object
spiderman = media.Movie("Spider Man",
                        "A boy is bitten by a spider and he becomes"
                        "a spiderman and starts saving the world",
                        "https://i.ytimg.com/vi/K4zm30yeHHE/maxresdefault.jpg",
                        "https://www.youtube.com/watch?v=DiTECkLZ8HM")
# this is instances or object
superman = media.Movie("Super Man",
                       "An alien orphan is sent from his dying planet"
                       "to Earth,"
                       "where he grows up to become superman",
                       "http://www.chicagonow.com/matthew-milams-films-and"
                       "-music/files/2016/12/Christopher-Reeve-"
                       "in-Superman.jpg",
                       "https://www.youtube.com/watch?v=T6DJcgm3wNY")
# this is instances or object
batman = media.Movie("Bat Man",
                     "Bat Man we all know him",
                     "https://cine.news/wp-content/uploads/"
                     "2017/10/ddhww74uqaahbfk-1004616.jpg",
                     "https://www.youtube.com/watch?v=qY3UkAHufLY")
# this is instances or object
ironman = media.Movie("Iron Man",
                      "Iron Man is a robotic movie created by marvel",
                      "https://vignette.wikia.nocookie.net/"
                      "marvelcinematicuniverse"
                      "/images/3/38/Tony_Stark_%28Official_IW_Concept_"
                      "Poster_-_Infobox_Crop%29.jpg/revision/latest/scale"
                      "-to-width-down/350?cb=20170731140930",
                      "https://www.youtube.com/watch?v=8hYlB38asDY")

# The list of movies in an array for displaying using fresh_tomatoes file
movies = [toy_story, wolf_story, spiderman, superman, batman, ironman]

# Opens movie page in the browser
fresh_tomatoes.open_movies_page(movies)
