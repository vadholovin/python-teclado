MENU_PROMPT = "\nEnter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie by title, or 'q' to quit: "
FIND_PROMPT = "\nEnter 't' to search by title, 'd' - by director, 'y' - by year: "
movies = []


def add_movie():
    title = input('Title: ')
    director = input('Director: ')
    year = input('Year: ')

    movies.append({
        "title": title,
        "director": director,
        "year": year,
    })


def show_movies():
    if len(movies):
        for counter, movie in enumerate(movies, start=1):
            title = movie["title"]
            director = movie["director"]
            year = movie["year"]
            output = f"{counter}. Title: {title}, " \
                     f"Director: {director}, " \
                     f"Release year: {year}"

            print(output)
    else:
        print("\nThe movie list is empty. Add a movie.")


find_movie_options = {
    't': 'title',
    'd': 'director',
    'y': 'year',
}


def find_movie():
    if len(movies) == 0:
        print("The movie list is empty. Add a movie.")
        return None

    q = input(FIND_PROMPT)

    if q in find_movie_options:
        search_option = find_movie_options[q]
        search_query = input("\nSearching for: ")
        counter = 0

        for movie in movies:
            title = movie["title"]
            director = movie["director"]
            year = movie["year"]

            if movie[search_option].lower() == search_query.lower():
                print(f"\nTitle: {title},\nDirector: {director},\nYear: {year}")
                counter += 1

        if counter == 0:
            print('Found no movies')

    else:
        print('Unknown command. Please try again.')


menu_options = {
    'a': add_movie,
    'l': show_movies,
    'f': find_movie
}


def show_menu(user_selection):
    while user_selection != 'q':
        if user_selection in menu_options:
            selected_option = menu_options[user_selection]
            selected_option()
        else:
            print('Unknown command. Please try again.')

        user_query = input(MENU_PROMPT)


selection = input(MENU_PROMPT)

show_menu(selection)
