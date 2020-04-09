class Movies:
    def __init__(self):
        self.movies = []

    def __len__(self):
        return len(self.movies)

    def __str__(self):
        return f"Collection contains {len(self.movies)} movies"

    @staticmethod
    def print_movie(movie):
        print(f"\nTitle: {movie['title']}")
        print(f"Director: {movie['director']}")
        print(f"Release year: {movie['year']}")

    def add(self, title, director, year):
        self.movies.append({
            'title': title,
            'director': director,
            'year': year,
        })

    def show_movies(self):
        for movie in self.movies:
            self.print_movie(movie)

    def search(self, search_title):
        for movie in self.movies:
            if search_title.lower() == movie['title'].lower():
                self.print_movie(movie)
                break
        else:
            print(f'Found nothing for <{search_title}>')


collection = Movies()
collection.add('Titanic', 'Cameron', 1995)
collection.add('Terminator', 'Spielberg', 1991)
collection.add('The Matrix', 'Lynch', 1998)

print(collection)
collection.search('titanic')
