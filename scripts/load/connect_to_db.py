import psycopg2

from config.constants import HOST, PORT, DB_USER, DB_PASS, DB



def connect_to_db():
    conn = psycopg2.connect(
        host=HOST,
        port=PORT,
        database=DB[0],
        user=DB_USER,
        password=DB_PASS
    )

    db = conn.cursor()
    return [db,conn]

def connect_to_main_db():
    conn = psycopg2.connect(
        host=HOST,
        port=PORT,
        database=DB[1],
        user=DB_USER,
        password=DB_PASS
    )
    db = conn.cursor()
    return [db,conn]
