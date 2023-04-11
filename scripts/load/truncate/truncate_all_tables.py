
from scripts.load.truncate.truncate import truncate
from scripts.load.truncate.tables_to_truncate import all_tables_to_truncate


def truncate_all_tables(): 
    for ds in all_tables_to_truncate:
        _ds = ds
        sql = "Truncate table "+ _ds +';'
        truncate(sql)
    print("✅  Truncate completed")
