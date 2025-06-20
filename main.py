# Code for vertices and what they represent
vertices = {0  : "Main Gate",
            1  : "Car Park",
            2  : "Entrance Shaded Path",
            3  : "Lecturer's Dormitory",
            4  : "Reading Room Shaded Path",
            5  : "Labtek 5",
            6  : "IPST",
            7  : "Metallurgy Lab",
            8  : "Motorcycle Park",
            9  : "GKU 2 Shaded Path",
            10 : "Labtek 1B",
            11 : "Labtek 1A",
            12 : "Sedimentation Lab",
            13 : "Rectorate Parking Lot",
            14 : "Main Buildings",
            15 : "North FTI Building",
            16 : "GOR Futsal",
            17 : "GOR Tenis Meja"
            }

# Graph represented by adjacency list using dictionary
# Source vertex as key, tuple of destination and distance as value
graph = {   0  : [(2, 53.01)],
            1  : [(2, 55.83)],
            2  : [(0, 53.01), (1, 55.83), (3, 216.03), (7, 29.81), (8, 21.4), (9, 11.86), (12, 134.42)],
            3  : [(2, 216.03), (4, 221.42)],
            4  : [(3, 221.42), (5, 13.32), (6, 17.11), (14, 29.42), (13, 89.51)],
            5  : [(4, 13.32)], 
            6  : [(4, 17.11)],
            7  : [(2, 29.81)],
            8  : [(2, 21.4)],
            9  : [(2, 11.86), (14, 9.27)],
            10 : [(11, 53.07), (14, 31.2), (12, 95.98)],
            11 : [(10, 53.07), (12, 72.5), (14, 13.42)],
            12 : [(10, 95.98), (11, 72.5), (2, 134.42), (14, 104.3)],
            13 : [(14, 59.38), (4, 89.51)],
            14 : [(4, 29.42), (9, 9.27), (10, 31.2), (11, 13.42), (12, 104.3), (13, 59.38), (15, 18.87), (16, 10.31)],
            15 : [(14, 18.87)],
            16 : [(14, 10.31), (17, 20.44)],
            17 : [(16, 20.44)]
            }

# Create sorted list of edges (tuple of source, destination, and distance)
def sortEdges(graph : dict) -> list:
    edges = []
    for source in graph.keys():
        for adj in graph.get(source):
            dest = adj[0]
            dist = adj[1]
            edge = set([source, dest])
            if (edge, dist) not in edges:
                edges.append((edge, dist))
    return sorted(edges, key=lambda x: x[1])

# DFS utility function for cycle-finding
def dfs(graph : dict, visited : set, parent : int, v : int) -> bool:
    visited.add(v)
    edges = graph[v]
    for edge in edges:
        if edge[0] not in visited:
            if dfs(graph, visited, v, edge[0]):
                return True
        elif parent != edge[0]:
            return True
    return False

# Function to check for cycle within a graph
def containCycle(graph : dict) -> bool:
    visited = set()
    for vertex in graph.keys():
        if vertex not in visited:
            if dfs(graph, visited, -1, vertex):
                return True
    return False

# Kruskal algorithm on a graph, returns a tuple of minimum weight spanning tree and its weight
def kruskal(graph : dict) -> tuple:
    # Create empty graph with same vertices as the original graph
    spanning_tree = dict()
    for vertex in graph.keys():
        spanning_tree[vertex] = []
    total_distance = 0.0
    
    # Sort edges by distance ascending
    edges = sortEdges(graph)

    # Add edge if it doesn't create cycle, starting from the smallest distance
    for edge in edges:
        v1 = min(edge[0])
        v2 = max(edge[0])
        print(f"{v1} {v2} {edge[1]}")
        temp1 = spanning_tree.get(v1)
        temp1.append((v2, edge[1]))
        temp2 = spanning_tree.get(v2)
        temp2.append((v1, edge[1]))
        spanning_tree[v1] = temp1
        spanning_tree[v2] = temp2

        if (containCycle(spanning_tree)):
            temp1.remove((v2, edge[1]))
            temp2.remove((v1, edge[1]))
            spanning_tree[v1] = temp1
            spanning_tree[v2] = temp2
        else:
            total_distance += edge[1]

    return (spanning_tree, total_distance)

result = kruskal(graph)
print(f"Spanning tree length: {result[1]}")
for key in result[0].keys():
    print(f"{key} : ", end="")
    succ = result[0].get(key)
    for i in range(len(succ)):
        dest = succ[i][0]
        if i != 0:
            print(", ", end="")
        print(dest, end="")
    print()
# for key in result[0].keys():
#     print(f"{vertices[key]} : ", end="")
#     succ = result[0].get(key)
#     for i in range(len(succ)):
#         dest = succ[i][0]
#         if i != 0:
#             print(", ", end="")
#         print(vertices[dest], end="")
#     print()