import matplotlib.pyplot as plt
import math

graph = {
    'A': {'B':4, 'C':6, 'D':5},
    'B': {'A':4, 'C':1, 'E':7},
    'C': {'A':6, 'B':1, 'D':2, 'E':5, 'F':4},
    'D': {'A':5, 'C':2, 'F':5},
    'E': {'B':7, 'C':5, 'F':1, 'G':6},
    'F': {'C':4, 'D':5, 'E':1, 'G':8},
    'G': {'E':6, 'F':8}
}

def dijkstra_table(graph, start):
    nodes = list(graph.keys())
    dist = {node: math.inf for node in nodes}
    visited = []
    dist[start] = 0
    parent = {node: None for node in nodes}

    print("\nDijkstra Table:\n")
    print("S\tS'\t\tA\tB\tC\tD\tE\tF\tG\tUi+1")

    while len(visited) < len(nodes):
        u = min((node for node in nodes if node not in visited), key=lambda x: dist[x])
        visited.append(u)

        for v, w in graph[u].items():
            if v not in visited and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                parent[v] = u

        dist_values = [dist[n] if dist[n] != math.inf else '∞' for n in nodes]
        next_node = None
        if len(visited) < len(nodes):
            next_node = min((node for node in nodes if node not in visited), key=lambda x: dist[x])

        print(f"{u}\t{' '.join(visited)}\t\t" + "\t".join(map(str, dist_values)) + f"\t{next_node}")

    return dist, parent

dist, parent = dijkstra_table(graph, 'A')

def get_path(parent, target):
    path = []
    while target:
        path.append(target)
        target = parent[target]
    return path[::-1]

target = 'G'
path = get_path(parent, target)

print("\nShortest Path:", path)
print("Total Distance:", dist[target])

pos = {
    'A': (0, 1),
    'B': (2, 3),
    'C': (2, 1),
    'D': (2, -1),
    'E': (4, 2),
    'F': (4, 0),
    'G': (6, 1)
}

edges = []
seen = set()
for u in graph:
    for v, w in graph[u].items():
        if (v, u) not in seen:
            edges.append((u, v, w))
            seen.add((u, v))

path_edges = list(zip(path, path[1:]))

def draw_graph(highlight=False):
    for u, v, w in edges:
        x = [pos[u][0], pos[v][0]]
        y = [pos[u][1], pos[v][1]]

        if highlight and ((u, v) in path_edges or (v, u) in path_edges):
            plt.plot(x, y, linewidth=3, color='red')
        else:
            plt.plot(x, y, color='black')

        mid_x = (pos[u][0] + pos[v][0]) / 2
        mid_y = (pos[u][1] + pos[v][1]) / 2
        plt.text(mid_x, mid_y, str(w), color='blue')

    for node, (x, y) in pos.items():
        plt.scatter(x, y, s=800)
        plt.text(x, y, node, ha='center', va='center', color='white')

    plt.axis('off')

plt.figure(figsize=(12,6))

plt.subplot(1,2,1)
draw_graph(False)
plt.title("Original Graph")

plt.subplot(1,2,2)
draw_graph(True)
plt.title("Shortest Path Highlighted")

plt.show()