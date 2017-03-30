import fresh_tomatoes
import media
# This is alist of my favourite movies
superman = media.Movie(
 "Superman",
 "A strong man resists the wrecked in the earth",
 "http://www.alsme.ca/sauveur.jpg",
 "https://www.youtube.com/watch?v=-DaPBBOHfsA")

xmen = media.Movie(
 "X-men",
 "Srangers men with superpower",
 "http://www.impawards.com/2016/posters/xmen_apocalypse_ver18_xxlg.jpg",
 "https://www.youtube.com/watch?v=Jer8XjMrUB4")

faceoff = media.Movie(
 "Faceoff",
 "A really real reality show",
 "http://screencrush.com/442/files/2016/06/face_off_xlg1.jpg?w=1600&cdnnode=1",
 "https://www.youtube.com/watch?v=5SVNLZXQcP0")

toy_story = media.Movie(
 "Toy Story",
 "A story of aboy and his toys that come to life",
 "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
 "https://www.youtube.com/watch?v=ZZv1vki4ou4")

ratatouille = media.Movie(
 "Ratatouille",
 "A rat is a chief in paris",
 "https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
 "https://www.youtube.com/watch?v=c3sBBRxDAqk")

doctor_strange = media.Movie(
 "Doctor strange",
 "A strange doctor in Adventures",
 "https://i.ytimg.com/vi/Bme-XHo-AA4/movieposter.jpg",
 "https://www.youtube.com/watch?v=Lt-U_t2pUHI")

# Put all of my movies in a list to pass it to the method(open_movies_page)
movies = [toy_story, doctor_strange, superman, ratatouille, xmen, faceoff]

# calling the method and pass movies to it
fresh_tomatoes.open_movies_page(movies)
