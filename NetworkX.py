import networkx as nx

G = nx.Graph()

G.add_nodes_from([1, 2, 3, 4])
G.add_edges_from([(1, 2), (2, 3), (3, 4), (1, 4)])

print("Узлы:", G.nodes())
print("Рёбра:", G.edges())

G.add_node(5)
G.add_edge(4, 5)

print("Узлы после добавления:", G.nodes())
print("Рёбра после добавления:", G.edges())

G.remove_node(2)
print("Узлы после удаления узла:", G.nodes())
print("Рёбра после удаления узла:", G.edges())
