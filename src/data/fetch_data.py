# -*- coding: utf-8 -*-
import os
import json
from zipfile import ZipFile


COMMAND = 'kaggle' \
          ' competitions download -c novozymes-enzyme-stability-prediction'
COMMAND2 = 'kaggle datasets download -d' \
           ' alejopaullier/aminoacids-physical-and-chemical-properties'


def fetch_kaggle_data(download_path, kaggle_json_path, command):
    """
    Function to extract the kaggle thata given a json with necesary
    credentials.

    Parameters
    ----------
    download_path: str
        String where data will be downloaded.
    kaggle_json_path: str
        String of the path where credentials are. Relative to the main path of
        the repo
    command: str
        Terminal instructions to run.

    Returns
    -------

    """
    with open(kaggle_json_path, 'r') as file:
        creds = json.load(file)
    os.environ['KAGGLE_USERNAME'] = creds['username']
    os.environ['KAGGLE_KEY'] = creds['key']
    os.chdir(download_path)
    os.system(command)

def extract_zip_files(file, extract_to):
    """
    Helper function to extract zip files from one zip folder into another
     folder.
    Parameters
    ----------
    file: str
        String of the path containing the zip file that will be extracted.
    extract_to:
        String of the path containing the new directory where all the
         extraction will be saved in.
    Returns
    -------
    """
    with ZipFile(file, 'r') as zip_f:
        zip_f.extractall(extract_to)
    return None


def main():
    actual_file_path = os.path.realpath(__file__)
    general_path = os.path.join(os.path.dirname(actual_file_path),'..','..')
    JSON_PATH = os.path.join(general_path, '../kaggle/kaggle.json')
    raw_data_path = os.path.join(general_path, 'data/raw')
    external_data_path = os.path.join(general_path, 'data/external')

    new_folder_path = os.path.join(raw_data_path, 'raw_kaggle_data')
    fetch_kaggle_data(
        download_path=raw_data_path,
        kaggle_json_path=JSON_PATH,
        command=COMMAND
    )
    os.chdir(general_path)
    file_name_path = [
        f'{raw_data_path}/{file}'
        for file in os.listdir(raw_data_path)
        if '.zip' in file
    ][0]
    extract_zip_files(file=file_name_path, extract_to=new_folder_path)

    fetch_kaggle_data(
        download_path=external_data_path,
        kaggle_json_path=JSON_PATH,
        command=COMMAND2
    )
    os.chdir(general_path)
    new_folder_path2 = os.path.join(external_data_path, './')
    file_name_path2 = [
        f'{external_data_path}/{file}'
        for file in os.listdir(external_data_path)
        if '.zip' in file
    ][0]
    extract_zip_files(file=file_name_path2, extract_to=new_folder_path2)


if __name__ == '__main__':
    main()
