"""Formatter module - formatting the tree with the selected formatter"""

from gendiff.formatters import get_formatter


def formatting(tree: dict, format_name="stylish") -> str:
    return get_formatter(format_name)(tree)
