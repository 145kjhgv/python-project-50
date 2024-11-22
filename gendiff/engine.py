import os

from gendiff.parser import parse


def get_file_extension(file_path: str) -> str:
    _, file_extension = os.path.splitext(file_path)
    return file_extension


def get_file_data(file_path: str) -> str:
    file_extension = get_file_extension(file_path)
    file_data = parse(file_path, file_extension)
    return file_data
