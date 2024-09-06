import json, random, statistics


def print_movie(movie):
    print(f"{movie['name']} ({movie['year']}): {movie['rating']}")


def print_list(movies):
    print(f"{len(movies)} movies in total")
    for movie in movies:
        print_movie(movie)


def get_year():
    while True:
        try:
            year = int(input("Enter the release year for this movie"))
            break
        except ValueError:
            print("Wrong input")
    return year


def get_rating():
    while True:
        try:
            rating = float(input("Enter a rating for this movie"))
            break
        except ValueError:
            print("Wrong input")
    return rating


def add_movie(movies):
    movie_name = input("Enter the name of the movie you want to add")
    for movie in movies:
        if movie['name'] == movie_name:
            print("This movie is already in our database")
            return
    year = get_year()
    rating = get_rating()
    movies.append({
        'name': movie_name,
        'year': year,
        'rating': rating
    })
    print("Movie added successfully")


def get_movie_id(movies, name):
    if len(name) < 1:
        return -1
    movie_id = -1
    for movie in movies:
        movie_id += 1
        if movie['name'] == name:
            return movie_id
    return -1


def delete_movie(movies):
    movie_name = input("Enter the name of the movie you want to delete")
    movie_id = get_movie_id(movies, movie_name)
    if movie_id >= 0:
        del movies[movie_id]
        print("The movie has been deleted from our database")
        return
    print("This movie is not present in our database")


def update_movie(movies):
    movie_name = input("Enter the name of the movie you want to update")
    movie_id = get_movie_id(movies, movie_name)
    if movie_id >= 0:
        movies[movie_id]['rating'] = get_rating()
        print("The movie has been updated successfully")
        return
    print("This movie is not present in our database")


def get_average_rating(movies):
    sum_ratings = 0
    for movie in movies:
        sum_ratings += movie['rating']
    return round(sum_ratings / len(movies), 1)


def get_median_rating(movies):
    rating_list = []
    for movie in movies:
        rating_list.append(movie['rating'])
    return statistics.median(rating_list)


def get_best_movies(movies):
    best_movies = []
    best_rating = 0
    for movie in movies:
        rating = movie['rating']
        if rating >= best_rating:
            best_rating = rating
            best_movies.append(movie)
    return best_movies


def get_worst_movies(movies):
    worst_movies = []
    worst_rating = 10
    for movie in movies:
        rating = movie['rating']
        if rating <= worst_rating:
            worst_rating = rating
            worst_movies.append(movie)
    return worst_movies


def get_stats(movies):
    average_rating = get_average_rating(movies)
    median_rating = get_median_rating(movies)
    best_movies = get_best_movies(movies)
    worst_movies = get_worst_movies(movies)
    print(f"The average rating is {average_rating}")
    print(f"The median rating is {median_rating}")
    print("The best movie(s): ")
    for movie in best_movies:
        print('\t', end='')
        print_movie(movie)
    print("The worst movie(s): ")
    for movie in worst_movies:
        print('\t', end='')
        print_movie(movie)


def get_random_movie(movies):
    key = random.randrange(len(movies))
    movie = movies[key]
    print_movie(movie)


def search_movie(movies):
    movie_name = input("Enter part of movie name:")
    movie_name = movie_name.lower()
    for movie in movies:
        if movie_name in movie['name'].lower():
            print_movie(movie)


def sort_by_year(movie):
    return movie['year']


def sort_by_rating(movie):
    return movie['rating']


def get_sorted_by_year(movies):
    movies.sort(key=sort_by_year)
    for movie in movies:
        print_movie(movie)


def get_sorted_by_rating(movies):
    movies.sort(key=sort_by_rating)
    for movie in movies:
        print_movie(movie)


def print_menu():
    print("""********** My Movies Database **********"\n
Menu:
0. Exit
1. List movies
2. Add movie
3. Delete movie
4. Update movie
5. Stats
6. Random movie
7. Search movie
8. Movies sorted by rating
9. Movies sorted by year
10. Filter movies
""")


def save_and_quit(movies):
    with open("data.json", "w") as fileobject:
        fileobject.write(json.dumps(movies))
    print("Bye!")


def main():
    # Dictionary to store the movies and the rating
    default_movies = [
        {
            'name': "In the Name of the Father",
            'year': 1993,
            'rating': 8.1
        },
        {
            'name': "Titanic",
            'year': 1997,
            'rating': 7.9
        },
        {
            'name': "The Shawshank Redemption",
            'year': 1994,
            'rating': 9.3
        },
        {
            'name': "The Godfather",
            'year': 1972,
            'rating': 9.2
        },
        {
            'name': "The Dark Knight",
            'year': 2008,
            'rating': 9.0
        },
        {
            'name': "Schindler's List",
            'year': 1993,
            'rating': 8.9
        },
        {
            'name': "Forrest Gump",
            'year': 1994,
            'rating': 8.8
        },
        {
            'name': "Pulp Fiction",
            'year': 1994,
            'rating': 8.9
        },
        {
            'name': "The Matrix",
            'year': 1999,
            'rating': 9.0
        },
        {
            'name': "Fight Club",
            'year': 1999,
            'rating': 8.8
        }
    ]

    try:
        with open("data.json", "r") as fileobject:
            movies = json.load(fileobject)
    except FileNotFoundError:
        movies = default_movies

    choices = {
        '1': print_list,
        '2': add_movie,
        '3': delete_movie,
        '4': update_movie,
        '5': get_stats,
        '6': get_random_movie,
        '7': search_movie,
        '8': get_sorted_by_rating,
        '9': get_sorted_by_year
    }

    while True:
        print_menu()
        try:
            user_choice = input("Enter choice (1-9):")
            if user_choice == '0':
                save_and_quit(movies)
                break
            choices[user_choice](movies)
            _ = input("Press any key to continue")
        except KeyError:
            print("A correct input you shall type")


if __name__ == "__main__":
    main()
