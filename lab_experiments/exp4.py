import networkx as nx
import matplotlib.pyplot as plt

# Given degree sequence
deg_seq = [4, 3, 3, 2, 2, 2, 2]

# Create graph using Havel-Hakimi algorithm
graph = nx.havel_hakimi_graph(deg_seq)

# Circular layout
layout = nx.circular_layout(graph)

# Draw graph
plt.figure(figsize=(7,7))

nx.draw_networkx(
    graph,
    pos=layout,
    with_labels=True,
    node_color='skyblue',
    node_size=1200,
    edge_color='black',
    font_size=10
)

# Display degrees on console
print("Degrees of vertices:")
for node, degree in graph.degree():
    print(f"Vertex {node}: Degree {degree}")

plt.title("Graph for Degree Sequence (4,3,3,2,2,2,2)")
plt.axis('off')
plt.show()