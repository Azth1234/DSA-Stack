# -------- BICONNECTED COMPONENTS (Tarjan's Algorithm) --------
class Biconnected:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = {i: [] for i in range(vertices)}
        self.time = 0

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def bcc_util(self, u, parent, low, disc, st):
        children = 0
        disc[u] = low[u] = self.time
        self.time += 1

        for v in self.graph[u]:
            if disc[v] == -1:
                children += 1
                st.append((u, v))
                self.bcc_util(v, u, low, disc, st)

                low[u] = min(low[u], low[v])

                if (parent == -1 and children > 1) or (parent != -1 and low[v] >= disc[u]):
                    print("Biconnected Component:")
                    while st[-1] != (u, v):
                        print(st.pop(), end=" ")
                    print(st.pop())

            elif v != parent and low[u] > disc[v]:
                low[u] = disc[v]
                st.append((u, v))

    def find_bcc(self):
        disc = [-1] * self.V
        low = [-1] * self.V
        st = []

        for i in range(self.V):
            if disc[i] == -1:
                self.bcc_util(i, -1, low, disc, st)

                if st:
                    print("Biconnected Component:")
                    while st:
                        print(st.pop(), end=" ")
                    print()


# -------- DRIVER CODE --------

print("---- Biconnected Components ----")
g1 = Biconnected(5)
g1.add_edge(1, 0)
g1.add_edge(0, 2)
g1.add_edge(2, 1)
g1.add_edge(0, 3)
g1.add_edge(3, 4)
g1.find_bcc()