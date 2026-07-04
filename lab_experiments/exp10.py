import networkx as nx
import matplotlib.pyplot as plt

# Create graph
G = nx.Graph()

# Add vertices
nodes = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
G.add_nodes_from(nodes)

# Add edges of original graph
edges = [
    ('A', 'B'),
    ('B', 'C'),
    ('C', 'D'),
    ('D', 'E'),
    ('E', 'F'),
    ('F', 'G'),
    ('G', 'H'),
    ('H', 'A'),
    ('H', 'B'),
    ('B', 'D'),
    ('D', 'F'),
    ('F', 'H')
]

G.add_edges_from(edges)

# Fixed positions for proper shape
pos = {
    'A': (0, 3),
    'B': (2, 3),
    'C': (4, 3),
    'D': (4, 1),
    'E': (4, -1),
    'F': (2, -1),
    'G': (0, -1),
    'H': (0, 1)
}

# Hamiltonian Circuit
hamiltonian_edges = [
    ('A', 'B'),
    ('B', 'C'),
    ('C', 'D'),
    ('D', 'E'),
    ('E', 'F'),
    ('F', 'G'),
    ('G', 'H'),
    ('H', 'A')
]

# Create figure
plt.figure(figsize=(12, 6))

# ---------------- Original Graph ----------------
plt.subplot(1, 2, 1)

nx.draw(
    G,
    pos,
    with_labels=True,
    node_color='lightblue',
    node_size=1200,
    font_size=12,
    edge_color='black',
    width=2
)

edge_labels = {
    ('A', 'B'): 'e1',
    ('B', 'C'): 'e2',
    ('C', 'D'): 'e3',
    ('D', 'E'): 'e4',
    ('E', 'F'): 'e5',
    ('F', 'G'): 'e6',
    ('G', 'H'): 'e7',
    ('H', 'A'): 'e8',
    ('H', 'B'): 'e9',
    ('B', 'D'): 'e10',
    ('D', 'F'): 'e11',
    ('F', 'H'): 'e12'
}

nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

plt.title("Original Graph")

# ---------------- Hamiltonian Graph ----------------
plt.subplot(1, 2, 2)

nx.draw(
    G,
    pos,
    with_labels=True,
    node_color='lightgreen',
    node_size=1200,
    font_size=12,
    edge_color='lightgray',
    width=1
)

# Highlight Hamiltonian circuit
nx.draw_networkx_edges(
    G,
    pos,
    edgelist=hamiltonian_edges,
    edge_color='red',
    width=3
)

edge_labels = {
    ('A', 'B'): 'e1',
    ('B', 'C'): 'e2',
    ('C', 'D'): 'e3',
    ('D', 'E'): 'e4',
    ('E', 'F'): 'e5',
    ('F', 'G'): 'e6',
    ('G', 'H'): 'e7',
    ('H', 'A'): 'e8',
    ('H', 'B'): 'e9',
    ('B', 'D'): 'e10',
    ('D', 'F'): 'e11',
    ('F', 'H'): 'e12'
}

nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

plt.title("Hamiltonian Circuit")

plt.tight_layout()
plt.show()