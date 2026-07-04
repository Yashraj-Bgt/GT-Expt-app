import networkx as nx
import matplotlib.pyplot as plt

# Create graph
G = nx.Graph()

nodes = ["A","B","C","D","E","F","G","H"]
G.add_nodes_from(nodes)

# Outer square
edges = [
    ("A","B"), ("B","C"), ("C","D"), ("D","E"),
    ("E","F"), ("F","G"), ("G","H"), ("H","A")
]

# Inner diamond
edges += [
    ("B","D"), ("D","F"), ("F","H"), ("H","B")
]

G.add_edges_from(edges)

# Positions (to match your diagram)
pos = {
    "A": (0,2),
    "B": (1,2),
    "C": (2,2),
    "D": (2,1),
    "E": (2,0),
    "F": (1,0),
    "G": (0,0),
    "H": (0,1)
}

# Find Eulerian circuit
circuit = list(nx.eulerian_circuit(G))
circuit_edges = [(u,v) for u,v in circuit]

# Create figure with 2 subplots
fig, axes = plt.subplots(1, 2, figsize=(12,6))

# -------- Original Graph --------
nx.draw(G, pos, ax=axes[0], with_labels=True,
        node_color='lightblue', node_size=1000,
        edge_color='black', width=2)
axes[0].set_title("Original Graph")

# -------- Eulerian Circuit Graph --------
nx.draw(G, pos, ax=axes[1], with_labels=True,
        node_color='lightblue', node_size=1000,
        edge_color='lightgray', width=2)

# Highlight Eulerian circuit
nx.draw_networkx_edges(G, pos, ax=axes[1],
                       edgelist=circuit_edges,
                       edge_color='red', width=3)

axes[1].set_title("Eulerian Circuit")

plt.tight_layout()
plt.show()

# Print the circuit
print("Eulerian Circuit:")
for edge in circuit:
    print(edge)