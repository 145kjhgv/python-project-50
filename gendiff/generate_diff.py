def generate_diff(file_path1: str,
                  file_path2: str,
                  format_name="stylish") -> str:
    dict_1 = dict(get_file_data(file_path1))
    dict_2 = dict(get_file_data(file_path2))
    tree = build_tree(dict_1, dict_2)
    diff = formatting(tree, format_name)
    return diff
