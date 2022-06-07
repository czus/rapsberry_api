import sqlite3

movie_connection = sqlite3.connect(':memory:', check_same_thread=False)
cursor = movie_connection.cursor()

def cria_db():
    cursor.execute("DROP TABLE IF EXISTS Winners")
    sqlite_create_table_query = '''CREATE TABLE Winners (
                                id INTEGER PRIMARY KEY,
                                producer TEXT NOT NULL,
                                interval INT,
                                previousWin INT NOT NULL,
                                followingWin INT NOT NULL);'''

    cursor.execute(sqlite_create_table_query)
    movie_connection.commit()
    return cursor

def insert_db(producer, interval, previousWin, followingWin):
    movie_winner = [producer, interval, previousWin, followingWin]
    query_select = cursor.execute("SELECT * from Winners where producer=(?)", (producer,)).fetchall()
    if not query_select:
        cursor.execute('INSERT INTO Winners  (producer, interval, previousWin, followingWin) VALUES (?,?,?,?)', movie_winner)
        movie_connection.commit()
        print("Data updated on database.", cursor.rowcount)
    else:
        print("Data already exists on database.")


def select_max_winners():
    movies_select_query = """SELECT producer, interval, previousWin, followingWin FROM Winners order by interval desc limit 2 """
    count = cursor.execute(movies_select_query)
    movie_connection.commit()
    resultado_query = cursor.fetchall()
    return resultado_query

def select_min_winners():
    movies_select_query = """SELECT producer, interval, previousWin, followingWin FROM Winners order by interval asc limit 2 """
    count = cursor.execute(movies_select_query)
    movie_connection.commit()
    resultado_query = cursor.fetchall()
    return resultado_query

def search_producer(producer):
    print(f"Searching on database for producer: {producer}")
    movie_select_query = """SELECT * from Winners where producer = (?)"""
    cursor.execute("SELECT * from Winners where producer=(?)", (producer,))
    result = cursor.fetchall()
    print(result)
    return result


def search_all_producers():
    print(f"Searching on Database for producers.")
    cursor.execute("SELECT * from Winners")
    result = cursor.fetchall()
    print(result)
    return result

def update_producer(producer):
    print(f"Updating producer data. Producer: {producer}")
    values = ["'{}'".format(value) for value in producer.values()]
    print(f"{__name__}{values}")
    id = cursor.execute("SELECT id from Winners where producer=(?)", (producer['producer'],)).fetchone()
    if id:
        print(id[0])
        update_values = ", ".join("{} = {}".format(key, value) for key, value in zip(producer.keys(), values))
        cursor.execute(f"UPDATE Winners SET {update_values} WHERE id = {id[0]}")
        print("Producer data updated.")
        return "Producer data updated"
    else:
        return "Producer not found on database."

def delete(producer):
    count = cursor.execute("SELECT count(*) AS count FROM Winners WHERE producer=(?)",(producer,))
    result = cursor.execute("SELECT * from Winners where producer=(?)", (producer,))
    if result:
        print(result.fetchall())
    #if result:
        cursor.execute("DELETE FROM Winners WHERE producer = (?)",(producer,))
        print("Producer data removed.")
        return "Producer data removed."
    else:
        return "Producer not found."


if __name__ == '__main__':
    print(__name__)