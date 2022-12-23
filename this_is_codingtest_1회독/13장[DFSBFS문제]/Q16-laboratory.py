#Q16[연구소] 342p
from itertools import combinations


n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

virus_location = []
safety_location = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            virus_location.append((i, j))
        if graph[i][j] == 0:
            safety_location.append((i, j))

wall_combinations = list(combinations(safety_location, 3))

def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return False
    if graph[x][y] == 0:
        graph[x][y] = 2
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    return False
maximum = 0

for walls in wall_combinations:
    count = 0
    for i in range(3):
        x = walls[i][0]
        y = walls[i][1]
        graph[x][y] = 1
    for virus in virus_location:
        graph[virus[0]][virus[1]] = 0
        dfs(virus[0],virus[1])
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                count += 1
            if graph[i][j] == 2:
                graph[i][j] = 0
    maximum = max(maximum, count)
    for i in range(3):
        x = walls[i][0]
        y = walls[i][1]
        graph[x][y] = 0
    for virus in virus_location:
        graph[virus[0]][virus[1]] = 2

print(maximum)