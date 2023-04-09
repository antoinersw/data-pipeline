import psycopg2

from config.constants import HOST, PORT, DB_USER, DB_PASS, DB



def connect_to_db():
    conn = psycopg2.connect(
        host=HOST,
        port=PORT,
        database=DB,
        user=DB_USER,
        password=DB_PASS
    )

    db = conn.cursor()
    return [db,conn]
