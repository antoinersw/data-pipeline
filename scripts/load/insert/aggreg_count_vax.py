from scripts.load.connect_to_db import connect_to_db 
from scripts.sql.datamart_tables import datamart_tables

def insert(sql_statement):

    [db,conn]= connect_to_db()

    db.execute(sql_statement)
    conn.commit()

def make_datamart_table():

    for sql_statement in datamart_tables:
        insert(sql_statement)