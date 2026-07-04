import networkx as nx
import matplotlib.pyplot as plt

# ---------------- CREATE GRAPH ----------------
G = nx.Graph()

# Vertices
nodes = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
G.add_nodes_from(nodes)

# Edges exactly like uploaded graph
edges = [
    ('A', 'B'),
    ('B', 'C'),
    ('C', 'D'),
    ('D', 'E'),
    ('E', 'A'),

    ('A', 'C'),
    ('C', 'E'),
    

    ('A', 'D'),
    ('F', 'D'),
    ('C', 'F'),
    ('E', 'F'),

    ('F', 'G'),
    ('C', 'H')
]

G.add_edges_from(edges)

# ---------------- POSITIONS ----------------
# Arranged to match uploaded structure

pos = {
    'A': (-1, 1),
    'B': (1, 2),
    'C': (3, 1),
    'D': (3, -1),
    'E': (-1, -1),
    'F': (5, -1),

    'G': (7, -1),
    'H': (5, 1)
}

# ---------------- COLORS ----------------
vertex_colors = {
    'A': 'red',
    'B': 'blue',
    'C': 'green',
    'D': 'blue',
    'E': 'yellow',
    'F': 'red',
    'G': 'blue',
    'H': 'red'
}

color_list = [vertex_colors[node] for node in G.nodes()]

# ---------------- DRAW BOTH GRAPHS ----------------
plt.figure(figsize=(14, 7))

# -------- Original Graph --------
plt.subplot(1, 2, 1)

nx.draw(
    G,
    pos,
    with_labels=True,
    node_color='lightgray',
    node_size=1400,
    edge_color='black',
    font_size=12,
    font_weight='bold',
    width=2
)

plt.title("Original Graph", fontsize=14)

# -------- Vertex Colored Graph --------
plt.subplot(1, 2, 2)

nx.draw(
    G,
    pos,
    with_labels=True,
    node_color=color_list,
    node_size=1400,
    edge_color='black',
    font_size=12,
    font_weight='bold',
    width=2
)

plt.title("Vertex Colored Graph", fontsize=14)

plt.tight_layout()
plt.show()