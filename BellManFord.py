def bellman_ford(vertices, edges, source):
    # Step 1: Initialize distances
    distance = [float('inf')] * vertices
    distance[source] = 0

    # Step 2: Relax all edges V-1 times
    for _ in range(vertices - 1):
        for u, v, w in edges:
            if distance[u] != float('inf') and distance[u] + w < distance[v]:
                distance[v] = distance[u] + w

    # Step 3: Check for negative weight cycle
    for u, v, w in edges:
        if distance[u] != float('inf') and distance[u] + w < distance[v]:
            print("Graph contains a negative weight cycle")
            return

    # Print result
    print("Vertex   Distance from Source")
    for i in range(vertices):
        print(f"{i} \t\t {distance[i]}")


# Number of vertices
V = 5

# Edge list: (source, destination, weight)
edges = [
    (0, 1, -1),
    (0, 2, 4),
    (1, 2, 3),
    (1, 3, 2),
    (1, 4, 2),
    (3, 2, 5),
    (3, 1, 1),
    (4, 3, -3)
]


# Source vertex
source = 0

bellman_ford(V, edges, source)
