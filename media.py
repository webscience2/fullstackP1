# Class for storing Movie information
class Movie():
    """ A Movie object with common attributes trailer, poster, etc"""
    def __init__(self, title, poster, trailer, rating, genre): #constructor
        self.trailer_youtube_url=trailer
        self.title=title
        self.poster_image_url=poster
        self.genre=genre #lets extend with some other attributes
        self.rating=rating #rating for the movie 
