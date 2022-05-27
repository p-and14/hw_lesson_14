from flask import Flask, jsonify
from utils import search_movie, search_by_years, search_by_rating, search_by_genre
from logger import basic_logger


app = Flask("__name__")


@app.route("/movie/<title>")
def movie_page(title):
    try:
        basic_logger.info("Введётся поиск фильма по названию")
        movie = search_movie(title)
    except:
        basic_logger.error(f"{title} - фильма с таким названием не существует")
        return jsonify({"error": "Фильма с таким названием не существует"})
    else:
        basic_logger.info(f'Фильм "{title}" найден')
        return jsonify(movie)


@app.route("/movie/<year_before>/to/<year_after>")
def movie_by_year(year_before, year_after):
    try:
        basic_logger.info(f"Введётся поиск фильмов между {year_before} и {year_after} годами")
        movies = search_by_years(year_before, year_after)
    except:
        basic_logger.error(f"Некорректно введена дата {year_after, year_before}")
        return jsonify({"error": "Некорректно введена дата"})
    else:
        basic_logger.info(f"Фильмы между {year_before} и {year_after} годами найдены")
        return jsonify(movies)


@app.route("/rating/children")
def movie_by_children_rating():
    basic_logger.info('Введётся поиск фильмов c рейтингом "children"')

    movies = search_by_rating("children")

    basic_logger.info('Фильмы c рейтингом "children" найдены')
    return jsonify(movies)


@app.route("/rating/family")
def movie_by_family_rating():
    basic_logger.info('Введётся поиск фильмов c рейтингом "family"')

    movies = search_by_rating("family")

    basic_logger.info('Фильмы c рейтингом "family" найдены')
    return jsonify(movies)


@app.route("/rating/adult")
def movie_by_adult_rating():
    basic_logger.info('Введётся поиск фильмов c рейтингом "adult"')

    movies = search_by_rating("adult")

    basic_logger.info('Фильмы c рейтингом "adult" найдены')
    return jsonify(movies)


@app.route("/genre/<genre>")
def movie_by_genre(genre):
    basic_logger.info(f'Введётся поиск фильмов по жанру "{genre}"')

    movies = search_by_genre(genre)

    if movies:
        basic_logger.info(f'Фильмы по жанру "{genre}" найдены')
    else:
        basic_logger.info(f'Нет фильмов по жанру "{genre}"')
    return jsonify(movies)


if __name__ == "__main__":
    app.run()
