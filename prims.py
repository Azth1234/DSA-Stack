import heapq

def prim(graph, start):
    visited = set()
    min_heap = [(0, start, None)]  # (weight, node, parent)
    total_cost = 0
    mst_edges = []

    while min_heap:
        weight, node, parent = heapq.heappop(min_heap)

        if node in visited:
            continue

        visited.add(node)
        total_cost += weight

        if parent is not None:
            mst_edges.append((parent, node, weight))

        for neighbor, w in graph[node]:
            if neighbor not in visited:
                heapq.heappush(min_heap, (w, neighbor, node))

    return total_cost, mst_edges


# Example
graph = {
    'A': [('B', 2), ('C', 3)],
    'B': [('A', 2), ('C', 1), ('D', 4)],
    'C': [('A', 3), ('B', 1), ('D', 5)],
    'D': [('B', 4), ('C', 5)]
}

cost, mst = prim(graph, 'A')

print("Prim's MST cost:", cost)
print("Edges in MST:")
for u, v, w in mst:
    print(u, "-", v, "=", w)