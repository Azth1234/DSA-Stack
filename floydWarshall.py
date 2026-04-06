# Number of vertices
V = 5

# Edge list (source, destination, weight)
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

def floyd(V,edges):
    # Initialize distance matrix
    dist = [[float('inf')]*V for _ in range(V)]

    # Distance from node to itself = 0
    for i in range(V):
        dist[i][i] = 0

    # Fill matrix using edges
    for u, v, w in edges:
        dist[u][v] = w

    # Floyd–Warshall Algorithm
    for k in range(V):
        for i in range(V):
            for j in range(V):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    # Print result
    print("Shortest distance matrix:")
    for row in dist:
        print(row)


floyd(V,edges)