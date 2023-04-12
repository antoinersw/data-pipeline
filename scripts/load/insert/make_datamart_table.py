from scripts.load.insert.datamart_tables import datamart_tables
from scripts.load.insert.insert_table import insert


def make_datamart_table():

    for sql_statement in datamart_tables:
        insert(sql_statement)
