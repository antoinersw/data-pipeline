import schedule
import time

from scripts.extract.get_data_sources import get_data_sources
from scripts.sensors.check_files import check_files
from scripts.load.copy.copy_all_data_source_in_db import copy_all_data_source_in_db
from scripts.load.insert.aggreg_count_vax import make_datamart_table
from scripts.load.truncate.truncate_all_tables import truncate_all_tables
from scripts.clean.clean_up import clean_up


def job():
    print("job started...")
    # fetch data and put them in the data_sources_outdir
    get_data_sources()
    # check if files are in the right dir, if not error code is returned
    check_files()
    # truncate all tables
    truncate_all_tables()
    # copy files
    copy_all_data_source_in_db()
    print("all datas have been uploaded to the DB")
    # EXTRA : Create a datamart table based on copied files
    make_datamart_table()
    ##clean up
    clean_up()
   
    


schedule.every(5).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)

 