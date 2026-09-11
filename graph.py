import networkx as nx
import osmnx as ox
import matplotlib.pyplot as plt
import os
from collections import deque

# memakai sampel graph unej dan polije

output_dir = r"E:\Graph_Project\maps"
os.makedirs(output_dir, exist_ok=True)
plt.savefig(os.path.join(output_dir, "peta.png"), dpi=150, bbox_inches='tight')

center_lat = -8.1628
center_lon = 113.7199

print("Proses download.....")
G = ox.graph_from_point(
    (center_lat, center_lon),
    dist=2000,
    network_type='drive'
)

print("Proses download selesai.....")
print("node : ", len(G.nodes))
print("edge : ", len(G.edges))

# fasilkom y = -8.165890907246846, x = 113.71674493776341
# polije y = -8.159789089017243, x = 113.72300902061849

fasilkom = (113.71674493776341, -8.165890907246846) # array nya [x, y]
polije   = (113.72300902061849, -8.159789089017243)

awal = ox.distance.nearest_nodes(G, X=fasilkom[0], Y=fasilkom[1])
akhir = ox.distance.nearest_nodes(G, X=polije[0], Y=polije[1])

print(f"awal: {awal}")
print(f"akhir: {akhir}")

route = nx.shortest_path(G, source=awal, target=akhir, weight='length') # nyari rute lewat opensource
jauh = nx.shortest_path_length(G, source=awal, target=akhir, weight='length')
print(f"Jarak dari Fasilkom ke Polije itu {jauh}")

total_dist = 0
for u, v in zip(route[:-1], route[1:]):
    edge_data = G[u][v]
    # Ambil yang paling pendek/make metode bfs yang disediakan
    min_length = min(d.get('length', 0) for d in edge_data.values())
    total_dist += min_length

# kasih gambaran node dan edge nya
fig, ax = ox.plot_graph_route(
    G, route,
    route_color='red'
)

plt.savefig(os.path.join(output_dir, "peta_universitas.png"), dpi=150, bbox_inches='tight')
plt.show()