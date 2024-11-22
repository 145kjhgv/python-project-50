import json

import yaml


def parse(data: str, format: str) -> dict:
    match format:
        case 'yml' | 'yaml':
            return yaml.safe_load(data)
        case "json":
            return json.loads(data)
    raise ValueError(f"Unrecognized extension: {format}")
