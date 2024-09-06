import random
import statistics

menu = """********** My Movies Database **********"\n
Menu:
1. List movies
2. Add movie
3. Delete movie
4. Update movie
5. Stats
6. Random movie
7. Search movie
8. Movies sorted by rating
9. Quit
"""


def print_list(movies):
    print(f"{len(movies)} movies in total")
    for movie, rating in movies.items():
        print(f"{movie}: {rating}")


def add_movie(movies):
    movie_name = input("Enter the name of the movie you want to add")
    if movie_name in movies:
        print("This movie is already in our database")
        return
    rating = input("Enter a rating for this movie")
    movies[movie_name] = rating
    print("Movie added successfully")


def delete_movie(movies):
    movie_name = input("Enter the name of the movie you want to delete")
    if movie_name in movies:
        del movies[movie_name]
        print("The movie has been deleted from our database")
        return
    print("This movie is not present in our database")


def update_movie(movies):
    movie_name = input("Enter the name of the movie you want to update")
    if movie_name in movies:
        rating = input("Enter a new rating for this movie")
        movies[movie_name] = rating
        print("The movie has been updated successfully")
        return
    print("This movie is not present in our database")


def get_stats(movies):
    ratings = list(movies.values())
    ratings.sort(reverse=True)
    average = sum(ratings) / len(ratings)
    average = round(average, 1)
    median = statistics.median(ratings)
    best_movie = []
    worst_movie = []
    print(f"The average rating is {average}")
    print(f"The median rating is {median}")
    for movie in movies:
        if movies[movie] == ratings[0]:
            best_movie.append(movie)
        elif movies[movie] == ratings[-1]:
            worst_movie.append(movie)
    print("The best movie(s):", end='')
    for movie in best_movie:
        print(' - ', end='')
        print(movie, end='')
    print()
    print("The worst movie(s):", end='')
    for movie in worst_movie:
        print(' - ', end='')
        print(movie, end='')


def get_random_movie(movies):
    key = random.choice(list(movies.keys()))
    print(f"{key}: {movies[key]}")


def search_movie(movies):
    movie_name = input("Enter part of movie name:")
    movie_name = movie_name.lower()
    for movie in movies:
        if movie_name in movie.lower():
            print(f"{movie}: {movies[movie]}")


def get_sorted_movies(movies):
    sorted_movies = []
    ratings = list(movies.values())
    ratings.sort(reverse=True)
    for rating in ratings:
        for movie in movies:
            if movies[movie] == rating:
                if movie not in sorted_movies:
                    sorted_movies.append(movie)
    for movie in sorted_movies:
        print(f"{movie}: {movies[movie]}")


def main():
    # Dictionary to store the movies and the rating
    movies = {
        "The Shawshank Redemption": 9.5,
        "Pulp Fiction": 8.8,
        "The Room": 3.6,
        "The Godfather": 9.2,
        "The Godfather: Part II": 9.0,
        "The Dark Knight": 9.0,
        "12 Angry Men": 8.9,
        "Everything Everywhere All At Once": 8.9,
        "Forrest Gump": 8.8,
        "Star Wars: Episode V": 8.7
    }

    quit_menu = '9'
    user_choice = 0
    while user_choice != quit_menu:
        print(menu)
        user_choice = input("Enter choice (1-9):")
        match user_choice:
            case '1':
                print_list(movies)
            case '2':
                add_movie(movies)
            case '3':
                delete_movie(movies)
            case '4':
                update_movie(movies)
            case '5':
                get_stats(movies)
            case '6':
                get_random_movie(movies)
            case '7':
                search_movie(movies)
            case '8':
                get_sorted_movies(movies)
            case '9':
                print("Hasta la vista, baby")
            case _:
                print("A correct input you shall type")
        print()


if __name__ == "__main__":
    main()
