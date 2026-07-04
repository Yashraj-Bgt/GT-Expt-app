import networkx as nx
import matplotlib.pyplot as plt

# Create original graph
G = nx.Graph()

# Nodes
G.add_nodes_from([1, 2, 3, 4, 5, 6])

# Edges
G.add_edges_from([
    (1, 2),
    (2, 3),
    (3, 4),
    (4, 1),
    (1, 6),
    (2, 6),
    (6, 5),
    (5, 4),
    (1, 3)
])

# Fixed positions for consistent layout
pos = {
    1: (0, 0),
    2: (0, 2),
    3: (2, 2),
    4: (2, 0),
    5: (1.5, 1),
    6: (1, 0.4)
}

# 1. Spanning Subgraph
spanning = nx.Graph()
spanning.add_nodes_from(G.nodes())
spanning.add_edges_from([
    (2, 3),
    (4, 1),
    (2, 6),
    (6, 5),
    (5, 4),
    (1, 3)
])

# 2. Vertex Induced Subgraph
nodes_subset = [1, 2, 6]
induced = G.subgraph(nodes_subset).copy()

# 3. Edge Induced Subgraph
edge_subset = [(1, 6), (5, 4)]
edge_induced = nx.Graph()
edge_induced.add_nodes_from([1, 4, 5, 6])
edge_induced.add_edges_from(edge_subset)

# Plot all graphs
plt.figure(figsize=(12, 10))

# Original Graph
plt.subplot(2, 2, 1)
nx.draw(G, pos, with_labels=True,
        node_color='lightblue', node_size=800)
plt.title("Original Graph")

# Spanning Subgraph
plt.subplot(2, 2, 2)
nx.draw(spanning, pos, with_labels=True,
        node_color='lightgreen', node_size=800)
plt.title("Spanning Subgraph")

# Vertex Induced Subgraph
plt.subplot(2, 2, 3)
nx.draw(induced, pos, with_labels=True,
        node_color='orange', node_size=800)
plt.title("Vertex Induced Subgraph")

# Edge Induced Subgraph
plt.subplot(2, 2, 4)
nx.draw(edge_induced, pos, with_labels=True,
        node_color='pink', node_size=800)
plt.title("Edge Induced Subgraph")

plt.tight_layout()
plt.show()