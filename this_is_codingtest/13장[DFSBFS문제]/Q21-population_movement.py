#Q21[인구이동] 354p
from collections import deque

n, l, r = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def process(x, y, index):
    united = []
    united.append((x, y))
    q = deque()
    q.append((x, y))
    union[x][y] = index
    count = 1
    summary = graph[x][y]
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and union[nx][ny] == -1:
                if l <= abs(graph[x][y] - graph[nx][ny]) <= r:
                    q.append((nx, ny))
                    union[nx][ny] = index
                    united.append((nx, ny))
                    count += 1
                    summary += graph[nx][ny]
    for i, j in united:
        graph[i][j] = summary // count

total_count = 0

while True:
    union = [[-1] * n for _ in range(n)]
    index = -1
    for i in range(n):
        for j in range(n):
            if union[i][j] == -1:
                index += 1
                process(i, j, index)
    if index == n*n-1:
        break
    total_count += 1

print(total_count)