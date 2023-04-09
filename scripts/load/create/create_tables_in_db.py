from scripts.load.create.create_table import create_table
from config.tables_to_create import all_tables_to_create


def create_tables_in_db():
    for sql_statement in all_tables_to_create:
        create_table(sql_statement)


