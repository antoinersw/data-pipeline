import schedule
import time
from config.constants import REFRESH_RATE
from scripts.extract.get_data_sources import get_data_sources
from scripts.check.check_files import check_files
from scripts.load.copy.copy_all_data_source_in_db import copy_all_data_source_in_db
from scripts.load.truncate.truncate_all_tables import truncate_all_tables
from scripts.load.create.create_dimensions import create_dimensions
from scripts.load.insert.make_datamart_table import make_datamart_table
from scripts.load.create.create_first_tables_in_db import create_first_tables_in_db
from scripts.clean.clean_up import clean_up


def job():
    print("🕑 Refreshing datas...")
    # @todo => backup de la database
    # fetch data and put them in the data_sources_outdir. Can be modified in the constant file
    get_data_sources()
    # check if files are in the right dir, if not, stop the process.
    # @todo => Restart the process of data_fetching and send email if rety fails
    check_files()
    create_first_tables_in_db()
    # truncate necessary tables
    truncate_all_tables()
    # copy files from disk to postgres
    copy_all_data_source_in_db()
    # Create dimensions
    create_dimensions()
    # EXTRA : Create a datamart table based on copied files
    make_datamart_table()
    print("✅  Datamart is built")
    # clean up
    clean_up()
    print("🎇 Pipeline completed 🎇")


schedule.every(REFRESH_RATE).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
