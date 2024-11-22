from pathlib import Path

import pytest

from gendiff.scripts.gendiff import generate_diff

FIXTURES_DIR = f'{Path(__file__).parent}/fixtures'


def get_result_data(file_name):
    with open(f'{FIXTURES_DIR}/{file_name}') as output:
        return output.read()


@pytest.mark.parametrize(
    ('file1', 'file2'),
    [
        ('file1_tree.json', 'file2_tree.json'),
        ('file1_tree.yaml', 'file2_tree.yaml'),
    ]
)
def test_flat_diff(file1, file2):
    file1_path = f'{FIXTURES_DIR}/{file1}'
    file2_path = f'{FIXTURES_DIR}/{file2}'

    assert (generate_diff(file1_path, file2_path)
            == get_result_data('correct_result_tree.txt'))

    assert (generate_diff(file1_path, file2_path, 'stylish')
            == get_result_data('correct_result_tree.txt'))

    assert (generate_diff(file1_path, file2_path, 'plain')
            == get_result_data('correct_result_tree_plain.txt'))

    assert (generate_diff(file1_path, file2_path, 'json')
            == get_result_data('correct_result_tree_json.txt'))
