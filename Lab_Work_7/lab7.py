import csv

class DSU:
    def __init__(self, nodes):
        self.parent = {n: n for n in nodes}
        self.rank = {n: 0 for n in nodes}

    def find(self, i):
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            if self.rank[root_i] < self.rank[root_j]:
                self.parent[root_i] = root_j
            elif self.rank[root_i] > self.rank[root_j]:
                self.parent[root_j] = root_i
            else:
                self.parent[root_j] = root_i
                self.rank[root_i] += 1
            return True
        return False

def calculate_minimum_cable(filename):
    edges = []
    nodes = set()

    try:
        with open(filename, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                if not row:
                    continue
                u = row[0].strip()
                v = row[1].strip()
                w = int(row[2].strip())
                edges.append((w, u, v))
                nodes.add(u)
                nodes.add(v)
    except FileNotFoundError:
        return -1

    if not nodes:
        return 0

    edges.sort()
    dsu = DSU(nodes)
    min_cost = 0
    edges_used = 0

    for w, u, v in edges:
        if dsu.union(u, v):
            min_cost += w
            edges_used += 1

    if edges_used == len(nodes) - 1:
        return min_cost
    return -1

if __name__ == '__main__':
    result = calculate_minimum_cable('communication_wells.csv')
    print(result)