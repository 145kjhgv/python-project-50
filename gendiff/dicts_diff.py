def build_diff(parced_data1: dict, parced_data2: dict):
    diff = []
    sorted_keys = sorted(parced_data1.keys() | parced_data2.keys())

    for key in sorted_keys:
        match (key not in parced_data1, key not in parced_data2):
            case (True, False):
                diff.append({
                    'key': key,
                    'operation': 'add',
                    'new': parced_data2[key]
                })
            case (False, True):
                diff.append({
                    'key': key,
                    'operation': 'removed',
                    'old': parced_data1[key]
                })
            case (False, False):
                if (isinstance(parced_data1[key], dict)
                        and isinstance(parced_data2[key], dict)):
                    child = build_diff(parced_data1[key], parced_data2[key])
                    diff.append({
                        'key': key,
                        'operation': 'nested',
                        'value': child
                    })
                elif parced_data1[key] == parced_data2[key]:
                    diff.append({
                        'key': key,
                        'operation': 'same',
                        'value': parced_data1[key]
                    })
                else:
                    diff.append({
                        'key': key,
                        'operation': 'changed',
                        'old': parced_data1[key],
                        'new': parced_data2[key]
                    })

    return diff
