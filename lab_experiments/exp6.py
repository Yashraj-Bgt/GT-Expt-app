import networkx as nx
import matplotlib.pyplot as plt
import math

# ---------------- CREATE GRAPH ----------------

G = nx.Graph()

edges = [
    (0, 1, 7),
    (0, 3, 5),

    (1, 2, 8),
    (1, 3, 9),
    (1, 4, 7),

    (2, 4, 5),

    (3, 4, 15),
    (3, 5, 6),

    (4, 5, 8),
    (4, 6, 9),

    (5, 6, 11)
]

G.add_weighted_edges_from(edges)

# ---------------- NODE POSITIONS ----------------

pos = {
    0: (0, 3),
    1: (2, 3),
    2: (4, 3),

    3: (1, 2),
    4: (3, 2),

    5: (1.5, 1),
    6: (4, 1)
}

# ---------------- DRAW ORIGINAL GRAPH ----------------

plt.figure(figsize=(8, 6))

nx.draw(
    G,
    pos,
    with_labels=True,
    node_color='pink',
    node_size=1000,
    edgecolors="black"
)

labels = nx.get_edge_attributes(G, 'weight')

nx.draw_networkx_edge_labels(
    G,
    pos,
    edge_labels=labels
)

plt.title("Original Graph")

plt.gca().set_aspect('equal')

plt.show()

# ---------------- KRUSKAL ALGORITHM ----------------

parent = {}
rank = {}

def find(u):
    if parent[u] != u:
        parent[u] = find(parent[u])
    return parent[u]

def union(u, v):

    ru = find(u)
    rv = find(v)

    if ru == rv:
        return False

    if rank[ru] > rank[rv]:
        parent[rv] = ru

    elif rank[ru] < rank[rv]:
        parent[ru] = rv

    else:
        parent[rv] = ru
        rank[ru] += 1

    return True

# Initialize DSU

for node in G.nodes():
    parent[node] = node
    rank[node] = 0

# Sort edges according to weight

edges_sorted = sorted(edges, key=lambda x: x[2])

# MST Graph

mst = nx.Graph()

mst.add_nodes_from(G.nodes())

steps = []
selected_edges = []
total_cost = 0

# ---------------- BUILD MST ----------------

for u, v, w in edges_sorted:

    if union(u, v):

        mst.add_edge(u, v, weight=w)

        total_cost += w

        selected_edges.append((u, v))

        steps.append(list(selected_edges))

# ---------------- DRAW STEP BY STEP ----------------

cols = 3
rows = math.ceil(len(steps) / cols)

fig, axes = plt.subplots(rows, cols, figsize=(12, rows * 4))

axes = axes.flatten()

for i, step_edges in enumerate(steps):

    temp = nx.Graph()

    temp.add_nodes_from(G.nodes())

    temp.add_edges_from(step_edges)

    ax = axes[i]

    # Draw Nodes

    nx.draw_networkx_nodes(
        temp,
        pos,
        node_color='lightblue',
        node_size=500,
        edgecolors="black",
        ax=ax
    )

    # Draw Labels

    nx.draw_networkx_labels(
        temp,
        pos,
        font_size=10,
        ax=ax
    )

    # Previous edges

    prev_edges = step_edges[:-1]

    nx.draw_networkx_edges(
        temp,
        pos,
        edgelist=prev_edges,
        width=2,
        edge_color='black',
        ax=ax
    )

    # Current edge in RED

    curr_edge = [step_edges[-1]]

    nx.draw_networkx_edges(
        temp,
        pos,
        edgelist=curr_edge,
        width=3,
        edge_color='red',
        ax=ax
    )

    # Edge Labels

    edge_labels = {
        (u, v): G[u][v]['weight']
        for u, v in step_edges
    }

    nx.draw_networkx_edge_labels(
        temp,
        pos,
        edge_labels=edge_labels,
        font_size=8,
        ax=ax
    )

    ax.set_title(f"Step {i+1}")

    ax.set_aspect('equal')

    ax.axis('off')

# Hide extra subplots

for j in range(i + 1, len(axes)):
    axes[j].axis('off')

plt.tight_layout()

plt.show()

# ---------------- FINAL OUTPUT ----------------

print("Edges in MST:")

for u, v, w in mst.edges(data='weight'):
    print(f"{u} -- {v}  Weight = {w}")

print("\nTotal MST Cost =", total_cost)