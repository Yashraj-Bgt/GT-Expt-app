import networkx as nx
import matplotlib.pyplot as plt

edges = [
    ('A','B'), ('B','C'), ('C','D'), ('D','E'),
    ('E','F'), ('F','G'), ('G','H'), ('H','A'),
    ('B','D'), ('D','F'), ('F','H'), ('H','B')
]

G = nx.Graph()
G.add_edges_from(edges)

pos = {
    'A': (0,2), 'B': (1,2), 'C': (2,2),
    'H': (0,1), 'D': (2,1),
    'G': (0,0), 'F': (1,0), 'E': (2,0)
}

closed_walk = ['A','B','D','F','H','A','B','A']
closed_trail = ['A','B','D','F','H','A']
closed_path = ['B','C','D','F','H','B']

def create_subgraph(path):
    edges = [(path[i], path[i+1]) for i in range(len(path)-1)]
    G_sub = nx.Graph()
    G_sub.add_edges_from(edges)
    return G_sub

G_walk = create_subgraph(closed_walk)
G_trail = create_subgraph(closed_trail)
G_path = create_subgraph(closed_path)

fig, axes = plt.subplots(1, 4, figsize=(18,5))

nx.draw(G, pos, with_labels=True, node_color='lightgray', ax=axes[0])
axes[0].set_title("Original Graph")

nx.draw(G_walk, pos, with_labels=True, node_color='lightcoral', ax=axes[1])
axes[1].set_title("Closed Walk")

nx.draw(G_trail, pos, with_labels=True, node_color='lightblue', ax=axes[2])
axes[2].set_title("Closed Trail")

nx.draw(G_path, pos, with_labels=True, node_color='lightgreen', ax=axes[3])
axes[3].set_title("Closed Path")

plt.tight_layout()
plt.show()