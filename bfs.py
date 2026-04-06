def bfs_analysis(graph, start):
    n = len(graph)
    visited = [False] * n
    distance = [-1] * n
    queue = []

    cycle = False

    # Initialization
    visited[start] = True
    distance[start] = 0
    queue.append((start, -1))   # (node, parent)

    print("BFS Traversal Order:")

    while queue:
        current, parent = queue[0]
        queue = queue[1:]      # manual dequeue
        print(current, end=" ")

        for neighbor in graph[current]:
            if not visited[neighbor]:
                visited[neighbor] = True
                distance[neighbor] = distance[current] + 1
                queue.append((neighbor, current))

            elif neighbor != parent:
                cycle = True

    # Connectivity check
    connected = all(visited)

    print("\n\nShortest Distance from Source:")
    for i in range(n):
        print(f"Node {i} : {distance[i]}")

    print("\nGraph Connected:", connected)
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
bfs_analysis(graph, start_node)