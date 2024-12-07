import sys
from pathlib import Path
sys.path.append(f"{str(Path('.').absolute())}")

import os
from zipfile import ZipFile, ZIP_DEFLATED

from Utils import flow_logger, build_log_message, build_log_error


def save_file(file_name, file_content, directory='assets'):
    with open(f'{directory}/{file_name}', 'w') as file:
        file.write(file_content)
    return True

def copy_file(file_name: str, file_content: str) -> bool:
    with open(file_content, 'r') as file:
        content = file.read()

    with open(f'assets/{file_name}.py', 'w') as file:
        file.write(content)
    return True

def delete_files(files: list, directory='assets') -> bool:
    for file in files:
        os.remove(f'{directory}/{file}')
    return True

def save_zipfile(zip_name: str, file_names: list, file_dir: str, compression: str=ZIP_DEFLATED) -> bool:
    with ZipFile(f'assets/{zip_name}', 'w', compression) as zip:
        for file in os.listdir(file_dir):
            if file in file_names:
                zip.write(filename=f'{file_dir}/{file}', arcname=file)
    return True

def get_file_in_binary(file_name: str) -> str:
    with open(f'assets/{file_name}', 'rb') as file:
        content = file.read()
        return content