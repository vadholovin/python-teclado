MENU_PROMPT = "\nEnter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie by title, or 'q' to quit: "

movies = [
    {"title": "Titanic", "director": "Cameron", "year": "1995"},
    {"title": "Pulp Fiction", "director": "Tarantino", "year": "1997"},
    {"title": "Matix", "director": "Lynch", "year": "1998"},
    {"title": "Dead", "director": "Lynch", "year": "1995"},
]


def add_movie():
    title = input('Title: ')
    director = input('Director: ')
    year = input('Year: ')

    movies.append({
        "title": title,
        "director": director,
        "year": year,
    })


def show_movies(movies_list):
    if len(movies_list):
        for counter, movie in enumerate(movies_list, start=1):
            title = movie["title"]
            director = movie["director"]
            year = movie["year"]
            output = f"{counter}. Title: {title}, Director: {director}, Year: {year}"

            print(output)
    else:
        print("\nThe movie list is empty. Add a movie.")


def find_movie(movies_list):
    if len(movies_list) == 0:
        print("\nThe movie list is empty. Add a movie.")
        return None

    query_prompt = "\nEnter 't' for searching by title, 'd' - by director, 'y' - by year: "
    value_prompt = "\nSearching for: "
    queries = {
        't': 'title',
        'd': 'director',
        'y': 'year',
    }

    query = input(query_prompt)
    if query == 't' or query == 'd' or query == 'y':
        search_query = queries[query]
        search_value = input(value_prompt)
        counter = 0

        for movie in movies_list:
            title = movie["title"]
            director = movie["director"]
            year = movie["year"]

            if movie[search_query].lower() == search_value.lower():
                print(f"Title: {title}, Director: {director}, Year: {year}")
                counter += 1

        if counter == 0:
            print('Found no movies')
    else:
        print('Unknown command. Please try again.')


selection = input(MENU_PROMPT)

while selection != 'q':
    if selection == 'a':
        add_movie()
    elif selection == 'l':
        show_movies(movies)
    elif selection == 'f':
        find_movie(movies)
    else:
        print('Unknown command. Please try again.')

    selection = input(MENU_PROMPT)
