import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(filename: str,
                     delimeter: str = ',',
                     new_line: str = '\n'
                     ) -> list[dict]:
    # TODO ����������� ��������� �� csv � json
    with open(filename) as a:
        f = []
        for q, l in enumerate(a):
            k = l.strip(new_line).split(delimeter)
            if q == 0:
                z = k
                continue
            f.append({})
            for i, _ in enumerate(z):
                f[-1][z[i]] = k[i]
    return f


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))