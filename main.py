from pyvis.network import Network
import pandas as pd 
import networkx as nx 
import random
from cProfile import label
from os import path

data = pd.read_csv('data.csv',sep=';')
graph = nx.from_pandas_edgelist(data, source='Inviters',target='Name')
net = Network(notebook=True, height='2000px', width='100%', bgcolor='#222222', font_color='white')
# options ="""
# {
#   "layout": 
#   {
#     "hierarchical": 
#     {
#       "enabled": true,
#       "direction": "UD",
#       "nodeSpacing": 150,
#       "levelSeparation": 300,
#       "sortMethod": "directed",
#       "shakeTowards": "roots"
#     }
#   }
# }
# """
# net.set_options(options);
# net.show_buttons(filter_=['physics'])
net.from_nx(graph)

neighbor_map = net.get_adj_list()

# DISPLAY CONFIG
for node in net.nodes:        
    try:
        node['value'] = len(neighbor_map[node['id']])

        name = node['id']
        avatar_path = f'images/{name}.jpg'.lower()
        if path.exists(avatar_path):
            node['shape'] = 'circularImage'
            node['image'] = avatar_path

    except Exception as e:
        print(e)

# Adam special treatment     
node = net.get_node('Adam')
node['color'] = 'yellow'
node['size'] = 200

# Generate html
net.show('index.html')
