import os
from os.path import splitext

from gendiff.dicts_diff import build_diff
from gendiff.formatters import get_formatter
from gendiff.parser import parse


def get_file_extension(file_path: str) -> str:
    _, file_extension = os.path.splitext(file_path)
    return file_extension


def get_file_data(file_path: str) -> str:
    file_extension = get_file_extension(file_path)
    file_data = parse(file_path, file_extension)
    return file_data


def generate_diff(path_file1: str, path_file2: str,
                  formater: str = 'stylish') -> str:
    data1, format1 = prepare_data(path_file1)
    data2, format2 = prepare_data(path_file2)
    parced_data1 = parse(data1, format1)
    parced_data2 = parse(data2, format2)
    diff = build_diff(parced_data1, parced_data2)
    return get_formatter(formater)(diff)


EXTENSIONS = ('yaml', 'yml', 'json')


def prepare_data(path_file: str):
    extension = splitext(path_file)[1][1:]
    if extension in EXTENSIONS:
        with open(path_file) as f:
            data = f.read()
            return data, extension
    raise ValueError(f"Unrecognized extension: {extension}")
