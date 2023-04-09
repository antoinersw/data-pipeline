import os 
from config.data_sources import data_sources
from config.constants import DATA_SOURCES_OUTDIR


def check_files():
    for ds in data_sources:
        _ds = list(ds)[0]+".csv"
        full_path_to_check= DATA_SOURCES_OUTDIR+'/'+_ds 
        
        if os.path.isfile(full_path_to_check):
            print(f"The file {_ds} exists in the directory {full_path_to_check}.")
        else:
            print(f"The file {_ds} does not exist in the directory {full_path_to_check}.")
    