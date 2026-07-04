import networkx as nx
import matplotlib.pyplot as plt

# ---------------- CREATE GRAPH ----------------

G = nx.Graph()

edges = [
    ('A', 'B', 1),
    ('A', 'C', 2),
    ('B', 'C', 3),
    ('A', 'D', 4),
    ('A', 'E', 5),
    ('B', 'F', 6),
    ('C', 'F', 7),
    ('B', 'D', 8),
    ('C', 'E', 9),
    ('D', 'E', 10),
    ('D', 'F', 11),
    ('E', 'F', 12)
]

G.add_weighted_edges_from(edges)

# ---------------- NODE POSITIONS ----------------

pos = {
    'A': (0, 3),
    'B': (-2, 2),
    'C': (2, 2),
    'D': (-2, 0),
    'E': (2, 0),
    'F': (0, -2)
}

# ---------------- CREATE LINE GRAPH ----------------

L = nx.line_graph(G)

# ---------------- DRAW ORIGINAL GRAPH ----------------

plt.figure(figsize=(14, 6))

plt.subplot(1, 2, 1)

nx.draw(
    G,
    pos,
    with_labels=True,
    node_size=2000,
    node_color='lightblue',
    font_size=12,
    edgecolors='black'
)

edge_labels = nx.get_edge_attributes(G, 'weight')

nx.draw_networkx_edge_labels(
    G,
    pos,
    edge_labels=edge_labels,
    font_size=10
)

plt.title("Original Graph")

plt.axis('off')

# ---------------- DRAW LINE GRAPH ----------------

plt.subplot(1, 2, 2)

line_pos = nx.spring_layout(L, seed=42)

nx.draw(
    L,
    line_pos,
    with_labels=True,
    node_size=1800,
    node_color='lightgreen',
    font_size=8,
    edgecolors='black'
)

plt.title("Line Graph")

plt.axis('off')

# ---------------- SHOW OUTPUT ----------------

plt.tight_layout()

plt.show()