def dfs_analysis(graph, start):
    n = len(graph)
    visited = [0] * n   # 0 = unvisited, 1 = visiting, 2 = visited
    distance = [-1] * n
    topo = []
    cycle = False

    print("DFS Traversal Order:")

    def dfs(node, dist):
        nonlocal cycle
        visited[node] = 1
        distance[node] = dist
        print(node, end=" ")

        for neighbor in graph[node]:
            if visited[neighbor] == 0:
                dfs(neighbor, dist + 1)
            elif visited[neighbor] == 1:
                cycle = True

        visited[node] = 2
        topo.append(node)

    dfs(start, 0)

    print("\n\nDistance from Source (DFS Tree):")
    for i in range(n):
        print(f"Node {i} : {distance[i]}")

    topo.reverse()
    print("\nTopological Order:", topo)
    print("Cycle Present:", cycle)


# Graph (Adjacency List)
graph = [
    [1, 2],      # 0
    [0, 3, 4],   # 1
    [0, 5],      # 2
    [1],         # 3
    [1, 5],      # 4
    [2, 4]       # 5
]

start_node = 0
dfs_analysis(graph, start_node)