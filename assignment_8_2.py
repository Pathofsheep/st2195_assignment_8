# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 10:28:37 2022

@author: Patri
"""

#Practice assignment 8 part 2
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

trade_latest = pd.read_excel("N:\\Uni_Bigdata\\export_2020m1.xlsx", skiprows = 1, index_col= 0, nrows = 7)

pd.melt(trade_latest.reset_index(), id_vars = 'index')

trade_latest = pd.melt(trade_latest.reset_index(), id_vars = 'index')

trade_latest.columns = ['exp_ctry','imp_ctry','value']

trade_latest.dropna(inplace=True)

trade_latest.head()

trade_latest.shape

trade_latest.describe

G = nx.Graph()

for index, row in trade_latest.iterrows():
    G.add_edge(row['exp_ctry'], row['imp_ctry'], weight = row['value'])
# remove stuf

G.edges

G.nodes

G.edges(data=True)

#Draw the Graph

nx.draw(G, pos = nx.spring_layout(G))
nx.draw_networkx_labels(G, pos = nx.spring_layout(G))
plt.tight_layout()
plt.axis('off')
plt.show()

import pickle
f = open("graph_2020.pickle","wb")
pickle.dump(G,file=f)
f.close()