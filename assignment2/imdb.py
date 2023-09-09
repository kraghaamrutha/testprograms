
# importing json module
import json


def read_json_file(file_name):
    with open(file_name) as json_file:
        imdb_movie_data = json.load(json_file)
        # print data in pretty format
        # pretty_print_data = json.dumps(imdb_movie_data, indent=4, sort_keys=True)
        # print(f"Data: {pretty_print_data}")
    return imdb_movie_data


def top_dir_with_max_movies(file_name):
    imdb_movie_data = read_json_file(file_name)
    # write your logic here to solve the query


def popular_genere_watched_by_most(file_name):
    imdb_movie_data = read_json_file(file_name)
    # write your logic here to solve the query


def get_top_ten_movies_by_imdb_score(file_name):
    imdb_movie_data = read_json_file(file_name)
    # write your logic here to solve the query


def least_watched_movie_by_imdb_score(file_name):
    imdb_movie_data = read_json_file(file_name)
    # write your logic here to solve the query


def get_best_director_in_first_hundred_movies(file_name):
    imdb_movie_data = read_json_file(file_name)
    # write your logic here to solve the query


# check the data being returned by read_json_file
# print(read_json_file('imdb_movies.json'))

# print(top_dir_with_max_movies('imdb_movies.json'))
# print(popular_genere_watched_by_most('imdb_movies.json'))
# print(get_top_ten_movies_by_imdb_score('imdb_movies.json'))
# print(least_watched_movie_by_imdb_score('imdb_movies.json'))
# print(get_best_director_in_first_hundred_movies('imdb_movies.json'))
