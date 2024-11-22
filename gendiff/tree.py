from gendiff.make_tree import make_tree


def build_tree(dict_1: dict, dict_2: dict):
    return {
        'type': 'root',
        'children': make_tree(dict_1, dict_2)
    }
