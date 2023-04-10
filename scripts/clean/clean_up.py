from config.constants import DATA_SOURCES_OUTDIR
from config.data_sources import data_sources
import os
import sys
sys.path.append(os.path.abspath('../../'))


def clean_up():
    for ds in data_sources:
        _ds = list(ds)[0] + ".csv"
        full_path_to_check = DATA_SOURCES_OUTDIR + "/" + _ds

        if os.path.isfile(full_path_to_check):
           
            os.remove(full_path_to_check)

        else:
            print(
                f"The file {_ds} does not exist in the directory {full_path_to_check}.")
