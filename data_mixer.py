from pathlib import Path


def add_params(values: list[str], id, start, expertise, shared):
    return [
        str(id),
        values[start + 0],
        values[start + 1],
        values[start + 2],
        values[start + 3],
        values[start + 4],
        values[start + 5].strip(),
        expertise,
        shared,
    ]

def convert_data(values:list[str]):
    return [
        int(values[0]),
        values[1],
        float(values[2]),
        int(values[3]),
        int(values[4]),
        float(values[5]),
        float(values[6]),
        values[7],
        int(values[8]),
    ]

dest = open("dest.csv", "w")
destavg = open("dest-avg.csv", "w")
parameters = [
    "id",
    "strategy",
    "time",
    "rtask",
    "htask",
    "makespan",
    "risk",
    "expertise",
    "shared",
]
dest.write(", ".join(parameters) + "\n")
destavg.write(", ".join(parameters) + "\n")
id = 0

data = []

for csv_file in Path.cwd().joinpath("collected_data").iterdir():
    filename = csv_file.name
    shared = filename[0]
    expertise = "unexp" if "unexp" in filename else "exp"

    with csv_file.open() as src:
        content = src.readlines()[1:]

    if filename.endswith("-avg.csv"):
        destination = destavg
        start = 0
    else:
        destination = dest
        start = 1

    for line in content:
        values = add_params(line.split(", "), id, start, expertise, shared)

        destination.write(", ".join(values) + "\n")
        id += 1

        if start==1: data.append(convert_data(values))

dest.close()
destavg.close()