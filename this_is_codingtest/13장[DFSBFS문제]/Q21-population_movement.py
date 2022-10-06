#Q21[인구이동] 354p
from collections import deque

n, l, r = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, 1]

result = 0

def process(x, y, index):
    united = []
    united.append((x, y))
    union[x][y] = index
    q = deque()


total_count = 0
union = [[-1]*n for _ in range(n)]