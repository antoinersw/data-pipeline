from scripts.load.create.create_table import create_table
from scripts.load.create.tables_to_create import all_tables_to_create


def create_first_tables_in_db():
    for sql_statement in all_tables_to_create:
        create_table(sql_statement)
    print('✅  Base tables created in db')


