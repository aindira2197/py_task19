class Movie:
    def __init__(self, title, rating):
        self.title = title
        self.rating = rating

    def is_good(self):
        return self.rating >= 8

movie = Movie("Avatar", 9)

print(movie.is_good())
