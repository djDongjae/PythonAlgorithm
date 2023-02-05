def find_parent(parent, x):
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


v, e = map(int, input().split())
parent = [0] * v

for i in range(v):
    parent[i] = i

edges = []
result = 0

for _ in range(e):
    x, y, z = map(int, input().split())
    edges.append((z, x, y))

edges.sort()

total = 0
for edge in edges:
    cost, x, y = edge
    total += cost
    if find_parent(parent, x) != find_parent(parent, y):
        union_parent(parent, x, y)
        result += cost

print(total - result)