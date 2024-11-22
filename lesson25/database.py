import sqlite
import models

def create_connection():
    connection=sqlite.connect("movies.db")
    return connection
def create_table():
    connection=create_connection()
    cursor=connection.cursor()
    cursor.execute("""Create table if not exist movies( id integer primary key autoincrement, title text not null, director text notnull)""")

    connection.commit()
    connection.close()

create_table()

def create_movie(movie: models.MovieCreate):
    connection=create_connection()
    cursor=connection.cursor()
    cursor.execute("Insert into movies (titles, director) VALUES (?,?)",(movie.title, movie.director))
    connection.commit()
    movie_id=cursor.lastrowid
    connection.close()
    return movie_id

def read_movies():
    connection=create_connection()
    cursor= connection.cursor()
    cursor.execute("Select * from movies")
    rows= cursor.fetchall()
    movies= [models.Movie(id=row["id"], title=row["title"], director=row["director"])for row in rows]
    connection.close()
    return movies
def read_movie(movie_id: int):
    connection=create_connection()
    cursor=connection.cursor()
    cursor.execute("Select * from movies where id=?", (movie_id))
    row=cursor.fetchone()
    connection.close()
    if row is None:
        return None
    return models.Movie(id=row["id"], title=row["title"], director=row["director"])

def update_movie(movie_id:int, movie:models.MovieCreate):
    connection=create_connect()
    cursor=connection.cursor()
    cursor.execute("Update movies set title=?, director=? where id=?", (movie.title, movie.director, movie_id))
    connection.commit()
    updated= cursor.rowcount()
    connection.close()
    return updated>0


def delete_movie(movie_id:int):
    connection= create_connection()
    cursor=connection.cursor()
    cursor.execute("Delete from movies where id=?", (movie_id))
    connection.commit()
    deleted= cursor.rowcount
    connection.close()
    return deleted>0


