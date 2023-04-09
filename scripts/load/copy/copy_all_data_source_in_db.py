from scripts.load.copy.copy_tables import copy_tables
from config.tables_to_import import all_tables


def copy_all_data_source_in_db():
    for sql_statement in all_tables:
        copy_tables(sql_statement)


