#import dependencies
import webbrowser

#Defining the class for a movie which has four objects tile of the movie,story line, its image,urlfor trailer

class Movie():
    def __init__(self,movie_title,movie_storyline,movie_posterimage,movie_youtubetrailer):
        #Creating class for movie that stores the information of that movie a
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = movie_posterimage
        self.trailer_youtube_url = movie_youtubetrailer
        
    def show_trailer(self):
        #method Function to play the trailer for the given movie.
        webbrowser.open(self.youtube_trailer)# this is a method for the class movie
