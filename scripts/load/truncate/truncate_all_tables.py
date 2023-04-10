
from scripts.load.truncate.truncate import truncate
from config.tables_to_truncate import all_tables_to_truncate


def truncate_all_tables(): 
    for ds in all_tables_to_truncate:
        _ds = ds
        print(_ds)
        sql = "Drop table if exists "+ _ds +';'
        truncate(sql)

