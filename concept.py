from pyvis.network import Network
import pandas as pd 
import networkx as nx 
import random
from cProfile import label


data = pd.read_csv('data.csv',sep=';')

graph = nx.from_pandas_edgelist(data,source='Inviters',target='Name')
net = Network(notebook=True, height='2000px', width='100%', bgcolor='#222222', font_color='white')
# net.show_buttons(filter_=['physics'])
net.from_nx(graph)

neighbor_map = net.get_adj_list()
names_list = data['Inviters'].unique()

photos = dict(zip(data.Name,data.photo))

# DISPLAY CONFIG
for node in net.nodes:        
    try:
        node['value'] = len(neighbor_map[node["id"]])
        node['level'] = len(neighbor_map[node["id"]])

        if node['id'] in photos.keys() and type(photos[node['id']]) == str:
            node['shape'] = 'circularImage'
            node['image'] = photos[node['id']]

    except Exception as e:
        print(e)
        
node = net.get_node('Adam')
node['color'] = 'yellow'
node['shape'] = 'circularImage'
node['image'] = 'images/adam.jpg'
node['value'] = 90
node['size'] = 90


# Generate html
net.show('index.html')
