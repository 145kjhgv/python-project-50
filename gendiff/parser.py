import json

import yaml


def parse(data: str, extension: str) -> dict:
    match extension:
        case 'yml' | 'yaml':
            return yaml.safe_load(data)
        case "json":
            return json.loads(data)
    raise ValueError(f"Unrecognized extension: {extension}")
