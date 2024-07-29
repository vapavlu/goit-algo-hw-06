import networkx as nx
import matplotlib.pyplot as plt

# Створення графу
G = nx.Graph()

# Додавання вузлів (наприклад, станції метро)
nodes = ["Station1", "Station2", "Station3", "Station4", "Station5"]
G.add_nodes_from(nodes)

# Додавання ребер (зв'язки між станціями)
edges = [("Station1", "Station2"), ("Station1", "Station3"), ("Station2", "Station3"), ("Station3", "Station4"), ("Station4", "Station5")]
G.add_edges_from(edges)

# Візуалізація графу
plt.figure(figsize=(8, 6))
nx.draw(G, with_labels=True, node_color='skyblue', node_size=1500, edge_color='black', linewidths=1, font_size=15)
plt.title("Граф транспортної мережі")
plt.show()

# Аналіз основних характеристик
print("Кількість вершин:", G.number_of_nodes())
print("Кількість ребер:", G.number_of_edges())
print("Ступінь вершин:", dict(G.degree()))

def dfs(graph, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(set(graph[vertex]) - visited)
    return visited

def bfs(graph, start):
    visited, queue = set(), [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(set(graph[vertex]) - visited)
    return visited

# Виконання DFS та BFS
graph_dict = nx.to_dict_of_lists(G)
dfs_result = dfs(graph_dict, "Station1")
bfs_result = bfs(graph_dict, "Station1")

print("DFS результат:", dfs_result)
print("BFS результат:", bfs_result)

# Додавання ваг до ребер
weighted_edges = [("Station1", "Station2", 4), ("Station1", "Station3", 2), ("Station2", "Station3", 1), ("Station3", "Station4", 7), ("Station4", "Station5", 3)]
G.add_weighted_edges_from(weighted_edges)

# Реалізація алгоритму Дейкстри
def dijkstra(graph, start):
    shortest_paths = {start: (None, 0)}
    current_node = start
    visited = set()
    
    while current_node is not None:
        visited.add(current_node)
        destinations = graph[current_node]
        weight_to_current_node = shortest_paths[current_node][1]
        
        for next_node, weight_data in destinations.items():
            weight = weight_data['weight'] + weight_to_current_node
            if next_node not in shortest_paths:
                shortest_paths[next_node] = (current_node, weight)
            else:
                current_shortest_weight = shortest_paths[next_node][1]
                if current_shortest_weight > weight:
                    shortest_paths[next_node] = (current_node, weight)
        
        next_destinations = {node: shortest_paths[node] for node in shortest_paths if node not in visited}
        if not next_destinations:
            return shortest_paths
        current_node = min(next_destinations, key=lambda k: next_destinations[k][1])
        
    return shortest_paths

# Застосування алгоритму Дейкстри
dijkstra_result = dijkstra(G, "Station1")
print("Найкоротший шлях від Station1:", dijkstra_result)
