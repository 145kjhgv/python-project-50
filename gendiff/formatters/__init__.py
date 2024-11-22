from gendiff.formatters.constants import FORMATS
from gendiff.formatters.json import render_json
from gendiff.formatters.plain import render_plain
from gendiff.formatters.stylish import render_stylish


def get_formatter(formater):
    match formater:
        case FORMATS.STYLISH:
            return render_stylish
        case FORMATS.PLAIN:
            return render_plain
        case FORMATS.JSON:
            return render_json

    raise ValueError(f"Unrecognized formater: {formater}")
