# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 10:28:37 2022

@author: Patri
"""

#Practice assignment 8 part 3
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

trade_latest = pd.read_excel("N:\\Uni_Bigdata\\export_2021m1.xlsx", skiprows = 1, index_col= 0, nrows = 7)

pd.melt(trade_latest.reset_index(), id_vars = 'index')

trade_latest = pd.melt(trade_latest.reset_index(), id_vars = 'index')

trade_latest.columns = ['exp_ctry','imp_ctry','value']

trade_latest.dropna(inplace=True)

trade_latest.head()

trade_latest.shape

trade_latest.describe

G_last_year = nx.Graph()

for index, row in trade_latest.iterrows():
    G_last_year.add_edge(row['exp_ctry'], row['imp_ctry'], weight = row['value'])
# remove stuf

G_last_year.edges

G_last_year.nodes

G_last_year.edges(data=True)

#Draw the Graph

nx.draw(G_last_year, pos = nx.spring_layout(G_last_year))
nx.draw_networkx_labels(G_last_year, pos = nx.spring_layout(G_last_year))
plt.tight_layout()
plt.axis('off')
plt.show()

import pickle
f = open("graph_2020.pickle","rb")
G_2020 = pickle.load(f)
f.close()

options = {'width': 1,
           'node_color': 'lightblue'}


fig, ax  = plt.subplots(3, 2,figsize = (10,15))
layouts = {"spring": nx.spring_layout, "random": nx.random_layout, "circular": nx.circular_layout}
graphs = {"latest": G_2020, "last year": G_last_year}
for i, (layout_name,layout) in enumerate(layouts.items()):
    for j, (graph_name, graph) in enumerate(graphs.items()):
        position = layout(G_last_year)
        nx.draw_networkx(G_last_year, pos = position, ax=ax[i][j],font_size=9, **options)
        plt.tight_layout()
        ax[i][j].set_axis_off()
        ax[i][j].set_title(f"{layout_name} layout for {graph_name} data")