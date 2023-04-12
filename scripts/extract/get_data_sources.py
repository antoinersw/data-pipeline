import requests
import os
import csv
import pandas as pd
from io import StringIO
from config.data_sources import data_sources
from config.constants import DATA_SOURCES_OUTDIR


def move_csv_to_dir(ds_name, csv_file, out_directory):
    # Create the output directory if it doesn't exist
    if ds_name == False or csv_file == False:
        print("Error: Invalid input parameter")
        return

    file_name = ds_name + ".csv"
    # Create the output directory if it doesn't exist
    if not ds_name or not csv_file:
        print("Error: Invalid input parameter")
        return
    # Create the output directory if it doesn't exist
    os.makedirs(out_directory, exist_ok=True)
    output_path = os.path.join(out_directory, file_name)
    # Define the output file path and open it in write mode
    with open(output_path, 'w', newline='', encoding='utf-8') as output_file:
        # Create a CSV writer object and write the CSV data to the output file
        writer = csv.writer(output_file)
        for row in csv_file.splitlines():
            if ds_name == "vaccination_centers":
                writer.writerow(row.split(';'))
            else:
                writer.writerow(row.split(','))


def normalize_csv(ds_name, csv_text):
    # Use StringIO to create a file-like object from the csv_text variable
    csv_file = StringIO(csv_text)

    if ds_name == "vaccination_centers":

        # Read the csv file into a pandas DataFrame
        df = pd.read_csv(csv_file, sep=';', quoting=csv.QUOTE_MINIMAL,
                         on_bad_lines='skip', encoding='utf-8')
        # Write the normalized output to a new csv file

        move_csv_to_dir(ds_name, df.to_csv(index=False, sep=';',
                        doublequote=True, encoding='utf-8'), DATA_SOURCES_OUTDIR)
    else:
        # Read the csv file into a pandas DataFrame
        df = pd.read_csv(csv_file, low_memory=False, quoting=csv.QUOTE_MINIMAL,
                         sep=",", on_bad_lines='skip', encoding='utf-8')
        

        
        # Write the normalized output to a new csv file
        move_csv_to_dir(ds_name, df.to_csv(
            index=False, doublequote=True, encoding='utf-8'), DATA_SOURCES_OUTDIR)

    return df


def get_single_data(ds_obj):
    ds_name = next(iter(ds_obj.keys()))
    header = {'Content-Type': 'text/csv; charset=utf-8'}
    response = requests.get(ds_obj[ds_name], headers=header)
    # Decode the response text using the detected encoding
    response.encoding = 'utf-8'
    if response.status_code == 200:
        csv_text = response.text.replace('"', '')
        normalize_csv(ds_name, csv_text)
        return True
    else:
        print('Request failed, check your connection')
        return False
    


def get_data_sources():
    for sources in data_sources:
        get_single_data(sources)
    print("✅  Data souces collected")
