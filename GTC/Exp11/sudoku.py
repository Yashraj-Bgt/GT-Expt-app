import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
sudoku_board = [
    [3, 0, 0, 0],
    [0, 0, 0, 3],
    [0, 0, 0, 0],
    [0, 3, 4, 2]
]
G = nx.Graph()
for v in range(1, 17):
    G.add_node(v)
def vertex(row, col):
    return row * 4 + col + 1
for row in range(4):
    for col1 in range(4):
        for col2 in range(col1 + 1, 4):
            G.add_edge(vertex(row, col1), vertex(row, col2))
for col in range(4):
    for row1 in range(4):
        for row2 in range(row1 + 1, 4):
            G.add_edge(vertex(row1, col), vertex(row2, col))
for box_row in range(2):
    for box_col in range(2):
        cells = []
        for r in range(box_row * 2, box_row * 2 + 2):
            for c in range(box_col * 2, box_col * 2 + 2):
                cells.append(vertex(r, c))
        for i in range(len(cells)):
            for j in range(i + 1, len(cells)):
                G.add_edge(cells[i], cells[j])
forced_colors = {}
for row in range(4):
    for col in range(4):
        val = sudoku_board[row][col]
        if val != 0:
            forced_colors[vertex(row, col)] = val - 1
raw_coloring = nx.coloring.greedy_color(G, strategy="saturation_largest_first")
coloring = dict(raw_coloring)
for v, c in forced_colors.items():
    coloring[v] = c
changed = True
while changed:
    changed = False
    for node in G.nodes():
        if node in forced_colors:
            continue
        neighbor_colors = {coloring[nb] for nb in G.neighbors(node)}
        if coloring[node] in neighbor_colors:
            c = 0
            while c in neighbor_colors:
                c += 1
            coloring[node] = c
            changed = True
solved_board = [[0] * 4 for _ in range(4)]
for row in range(4):
    for col in range(4):
        solved_board[row][col] = coloring[vertex(row, col)] + 1
color_names = {0: "Red", 1: "Green", 2: "Blue", 3: "Yellow"}
print("=" * 35)
print("   Vertex  :  Degree")
print("=" * 35)
for node in G.nodes():
    print(f"   {node:<8}:  {G.degree(node)}")
print("=" * 35)
print()
print("=" * 35)
print("   Vertex  :  Assigned Colour")
print("=" * 35)
for node in sorted(coloring.keys()):
    print(f"   {node:<8}:  {color_names[coloring[node]]}")
print("=" * 35)
print()
print("=" * 35)
print("   Solved Sudoku Grid")
print("=" * 35)
for row in solved_board:
    print("   " + "  ".join(str(v) for v in row))
print("=" * 35)
def validate_sudoku(board):
    for row in range(4):
        if sorted(board[row]) != [1, 2, 3, 4]:
            return False
    for col in range(4):
        if sorted([board[r][col] for r in range(4)]) != [1, 2, 3, 4]:
            return False
    for br in range(2):
        for bc in range(2):
            box = [board[br*2+r][bc*2+c] for r in range(2) for c in range(2)]
            if sorted(box) != [1, 2, 3, 4]:
                return False
    return True

print()
if validate_sudoku(solved_board):
    print("Solution valid: YES")
else:
    print("Solution valid: NO — check colouring logic")
row_edges_set = set()
for row in range(4):
    for col1 in range(4):
        for col2 in range(col1 + 1, 4):
            e = frozenset([vertex(row, col1), vertex(row, col2)])
            row_edges_set.add(e)
col_edges_set = set()
for col in range(4):
    for row1 in range(4):
        for row2 in range(row1 + 1, 4):
            e = frozenset([vertex(row1, col), vertex(row2, col)])
            col_edges_set.add(e)
sub_edges_set = set()
for box_row in range(2):
    for box_col in range(2):
        cells = []
        for r in range(box_row * 2, box_row * 2 + 2):
            for c in range(box_col * 2, box_col * 2 + 2):
                cells.append(vertex(r, c))
        for i in range(len(cells)):
            for j in range(i + 1, len(cells)):
                e = frozenset([cells[i], cells[j]])
                sub_edges_set.add(e)
col_only  = col_edges_set - row_edges_set
sub_only  = sub_edges_set - row_edges_set - col_edges_set
def to_tuples(edge_set):
    return [tuple(sorted(e)) for e in sorted(edge_set)]
row_edge_list = to_tuples(row_edges_set)
col_edge_list = to_tuples(col_only)
sub_edge_list = to_tuples(sub_only)
def assign_curvatures(edge_list, base_rad):
    """Return a list of (edge, rad) pairs with alternating-sign curvatures."""
    result = []
    for i, e in enumerate(edge_list):
        sign = 1 if i % 2 == 0 else -1
        result.append((e, sign * base_rad))
    return result

row_curved  = assign_curvatures(row_edge_list, 0.12)
col_curved  = assign_curvatures(col_edge_list, 0.30)
sub_curved  = assign_curvatures(sub_edge_list, 0.50)
pos = {}
for row in range(4):
    for col in range(4):
        v = vertex(row, col)
        pos[v] = (col * 3.0, (3 - row) * 3.0)

color_hex = {0: "#D94F4F", 1: "#4DB86B", 2: "#4A90D9", 3: "#E6C13D"}

node_colors = [color_hex[coloring[n]] for n in sorted(G.nodes())]

value_labels = {v: str(solved_board[(v - 1) // 4][(v - 1) % 4]) for v in G.nodes()}

vertex_labels = {v: str(v) for v in G.nodes()}
offset_pos = {v: (pos[v][0], pos[v][1] + 0.62) for v in G.nodes()}

fig, ax = plt.subplots(figsize=(12, 11))
ax.set_facecolor("#F8F8F8")
fig.patch.set_facecolor("#F8F8F8")

ax.set_title(
    "4×4 Sudoku — Vertex Colouring using DSATUR Algorithm\n"
    "Each vertex label: Sudoku Value  |  Small number above: Vertex ID",
    fontsize=13, fontweight="bold", color="#1A1A1A", pad=14
)

nx.draw_networkx_nodes(
    G, pos,
    node_color=node_colors,
    node_size=1600,
    edgecolors="#333333",
    linewidths=1.8,
    ax=ax
)

for (u, v), rad in row_curved:
    nx.draw_networkx_edges(
        G, pos,
        edgelist=[(u, v)],
        edge_color="#888888",
        width=1.0,
        arrows=True,
        arrowstyle="-",
        connectionstyle=f"arc3,rad={rad}",
        ax=ax
    )

for (u, v), rad in col_curved:
    nx.draw_networkx_edges(
        G, pos,
        edgelist=[(u, v)],
        edge_color="#5599CC",
        width=1.0,
        arrows=True,
        arrowstyle="-",
        connectionstyle=f"arc3,rad={rad}",
        ax=ax
    )

for (u, v), rad in sub_curved:
    nx.draw_networkx_edges(
        G, pos,
        edgelist=[(u, v)],
        edge_color="#CC7733",
        width=1.0,
        arrows=True,
        arrowstyle="-",
        connectionstyle=f"arc3,rad={rad}",
        ax=ax
    )

nx.draw_networkx_labels(
    G, pos,
    labels=value_labels,
    font_size=13,
    font_color="white",
    font_weight="bold",
    ax=ax
)

nx.draw_networkx_labels(
    G, offset_pos,
    labels=vertex_labels,
    font_size=7,
    font_color="#333333",
    ax=ax
)

legend_patches = [
    mpatches.Patch(color="#D94F4F", label="Red    → Value 1"),
    mpatches.Patch(color="#4DB86B", label="Green  → Value 2"),
    mpatches.Patch(color="#4A90D9", label="Blue   → Value 3"),
    mpatches.Patch(color="#E6C13D", label="Yellow → Value 4"),
]

leg = ax.legend(
    handles=legend_patches,
    loc="lower center",
    ncol=4,
    framealpha=0.85,
    facecolor="#EEEEEE",
    edgecolor="#AAAAAA",
    fontsize=9,
    title="Node Colour → Sudoku Value",
    title_fontsize=9
)
ax.axis("off")
plt.tight_layout()
plt.savefig("sudoku_graph.png", dpi=150, bbox_inches="tight",
            facecolor=fig.get_facecolor())
print("\nGraph saved as 'sudoku_graph.png'")
plt.show()