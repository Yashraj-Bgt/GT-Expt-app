import networkx as nx
import matplotlib.pyplot as plt

plt.figure(figsize=(12,6))

# -------- Graph 1 --------
G1 = nx.Graph()
G1.add_edges_from([
    ('a','c'),
    ('b','c'),
    ('b','d'),
    ('d','e'),
    ('a','e')
])

plt.subplot(1, 3, 1)
pos1 = {
    'a': (1, 3),
    'b': (0, 2),
    'c': (0, 0),
    'd': (1, -1),
    'e': (2, 1)
}
nx.draw(G1, pos1, with_labels=True, node_size=800)
plt.title("Graph G1")
plt.axis('off')


# -------- Graph 2 --------
G2 = nx.Graph()
G2.add_edges_from([
    (1,2),
    (2,3),
    (3,4),
    (4,1),
    (5,2),
])

plt.subplot(1, 3, 2)
pos2 = {
    1: (0, 2),
    2: (0, 0),
    3: (3, 0),
    4: (3, 2),
    5: (0, 1)
}
nx.draw(G2, pos2, with_labels=True, node_size=800)
plt.title("Graph G2")
plt.axis('off')


# -------- Graph 3 --------
G3 = nx.Graph()
G3.add_edges_from([
    ('w','x'),
    ('x','v'),
    ('v','u'),
    ('u','w'),
    ('w','y'),
])

plt.subplot(1, 3, 3)
pos3 = {
    'u': (0, 2),
    'w': (0, 0),
    'x': (2, 0),
    'v': (2, 2),
    'y': (1, 1)
}
nx.draw(G3, pos3, with_labels=True, node_size=800)
plt.title("Graph G3")
plt.axis('off')

plt.tight_layout()
plt.show()


# -------- Isomorphism Check --------
print("G1 and G2 are isomorphic:", nx.is_isomorphic(G1, G2))
print("G1 and G3 are isomorphic:", nx.is_isomorphic(G1, G3))
print("G1 and G3 are isomorphic:", nx.is_isomorphic(G2, G3))