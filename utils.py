import json
import sqlite3
from logger import sql_logger


def connect_sql(query):

    with sqlite3.connect("netflix.db") as con:
        sql_logger.info("Успешное подключение к базе данных")
        cur = con.cursor()
        cur.execute(query)

        sql_logger.info("Данные получены и возвращены")
        return cur.fetchall()


def search_movie(user_title):

    query = f"""
        SELECT title, country, release_year, listed_in, description
        FROM netflix
        WHERE title LIKE '%{user_title}%'
        ORDER BY release_year DESC 
        LIMIT 1
        """

    movie = connect_sql(query)

    if not movie:
        raise IndexError

    result = {
        "title": movie[0][0],
        "country": movie[0][1],
        "release_year": movie[0][2],
        "genre": movie[0][3],
        "description": movie[0][4]
    }

    return result


def search_by_years(year_before, year_after):

    query = f"""
            SELECT title, release_year
            FROM netflix
            WHERE release_year BETWEEN {year_before} AND {year_after}
            LIMIT 100
            """

    movies_by_year = connect_sql(query)
    result = []

    for row in movies_by_year:
        result.append({"title": row[0], "release_year": row[1]})

    return result


def search_by_rating(rating):

    if rating == "children":
        rating_list = ("G", "")
    elif rating == "family":
        rating_list = ("G", "PG", "PG-13")
    elif rating == "adult":
        rating_list = ("R", "NC-17")

    query = f"""
            SELECT title, rating, description
            FROM netflix
            WHERE rating != ""
            AND rating IN {rating_list}
            LIMIT 100
            """

    movies_by_rating = connect_sql(query)
    result = []

    for row in movies_by_rating:
        result.append({"title": row[0], "rating": row[1], "description": row[2]})

    return result


def search_by_genre(genre):

    query = f"""
            SELECT title, description
            FROM netflix
            WHERE listed_in LIKE '%{genre}%'
            ORDER BY release_year DESC 
            LIMIT 10
            """

    movies_by_genre = connect_sql(query)
    result = []

    for row in movies_by_genre:
        result.append({"title": row[0], "description": row[1]})

    return result


def search_by_cast(cast_name_1, cast_name_2):

    query = f"""
            SELECT "cast"
            FROM netflix
            WHERE "cast" LIKE '%{cast_name_1}%'
            AND "cast" LIKE '%{cast_name_2}%'
            """

    movies_by_cast = connect_sql(query)
    cast_list = []

    for row in movies_by_cast:
        cast = row[0].split(", ")
        cast_list.extend(cast)

    cast_list.remove(cast_name_1)
    cast_list.remove(cast_name_2)
    result = []

    for actor in cast_list:
        if cast_list.count(actor) > 2:
            result.append(actor)

    result = list(set(result))

    return result


def search_by_type_year_genre(show_type, year, genre):

    if type(year) != int:
        return "Указана неправильная дата"

    query = f"""
            SELECT title, description
            FROM netflix
            WHERE "type" LIKE '%{show_type}%'
            AND release_year = {year}
            AND listed_in LIKE '%{genre}%'
            """
    movies_by_type_year_genre = connect_sql(query)
    result = []

    for row in movies_by_type_year_genre:
        result.append({"title": row[0], "description": row[1]})

    return json.dumps(result)
