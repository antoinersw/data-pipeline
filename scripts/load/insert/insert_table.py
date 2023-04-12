from scripts.load.connect_to_db import connect_to_db 

def insert(sql_statement):

    [db,conn]= connect_to_db()

    db.execute(sql_statement)
    conn.commit()
    conn.close()