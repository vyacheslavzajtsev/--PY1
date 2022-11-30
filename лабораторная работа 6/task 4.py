import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(filename: str,
                     delimeter: str = ',',
                     new_line: str = '\n'
                     ) -> list[dict]:
    # TODO реализовать конвертер из csv в json
    with open(filename) as a:
        fl = []
        for q, l in enumerate(a):
            k = l.strip(new_line).split(delimeter)
            if q == 0:
                z = k
                continue
            fl.append({})
            for i, _ in enumerate(z):
                fl[-1][z[i]] = k[i]

    return fl


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
