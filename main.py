MENU_PROMPT = "\nEnter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie by title, or 'q' to quit: "
movies = []


def add_movie():
    title = input("Enter the movie title: ")
    director = input("Enter the movie director: ")
    year = input("Enter the movie release year: ")

    movies.append({
        'title': title,
        'director': director,
        'year': year
    })


def show_movies():
    for movie in movies:
        print_movie(movie)


def print_movie(movie):
    print(f"Title: {movie['title']})")
    print(f"Director: {movie['director']}")
    print(f"Release year: {movie['year']}")


def find_movie():
    search_title = input("Enter movie title you are looking for: ")
    from math import e

    e = 1

    def func_1():
        e = 0

        def func_2():
            e = -1

            def func_3():
                e = 10
                print(e)

            func_3()

        func_2()

    func_1()
    Assume
    that
    func_1()
    will
    be


