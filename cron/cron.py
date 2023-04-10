import schedule
import time
from config.constants import REFRESH_RATE
from scripts.extract.get_data_sources import get_data_sources
from scripts.sensors.check_files import check_files
from scripts.load.copy.copy_all_data_source_in_db import copy_all_data_source_in_db
from scripts.load.create.create_dimensions import create_dimensions
from scripts.load.insert.aggreg_count_vax import make_datamart_table
from scripts.load.create.create_first_tables_in_db import create_first_tables_in_db
from scripts.clean.clean_up import clean_up


def job():
    print("🕑 Refreshing datas...")
    # fetch data and put them in the data_sources_outdir. Can be modified in the constant file
    get_data_sources()
    # check if files are in the right dir, if not, stop the process.
    # @todo => Restart the process of data_fetching and send email if rety fails
    check_files()
    print("✅  Files are in the correct folder")
    create_first_tables_in_db()
    print('✅  Base tables created in db')
    # copy files from disk to postgres
    copy_all_data_source_in_db()
    print("✅  All datas sources have been uploaded to the DB")
    # Create dimensions
    create_dimensions()
    print("✅  All dimensions have been created")
    # EXTRA : Create a datamart table based on copied files
    print("✅  Datamart is built")
    # clean up
    clean_up()
    print('✅  Clean up completed')
    print("🎇 Pipeline completed 🎇")


schedule.every(REFRESH_RATE).hours.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
