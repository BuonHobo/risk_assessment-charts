from pathlib import Path
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import graphs
from inspect import getmembers, isfunction

src_folder = "data"
dst_folder = "graphs"

for csv in Path(src_folder).iterdir():
    graph_dst = Path(dst_folder).joinpath(csv.name)
    graph_dst.mkdir(exist_ok=True, parents=True)

    data = pd.read_csv(csv)
    data['human foam'] = 6 - data['robot foam']
    data['human wood'] = 6 - data['robot wood']
    data['human metal'] = 6 - data['robot metal']
    data['collision score'] = 2 * data['foam collisions'] + 5 * data['wood collisions'] + 8 * data['metal collisions']

    for name, graph in getmembers(graphs, isfunction):
        graph(data, graph_dst.joinpath(name))
