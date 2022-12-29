import sys

input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)
visited = [False] * (n + 1)
start = int(input())

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))  # b: 연결된 노드, c: 노드 간의 거리


def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1, n + 1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index


def dijkstra(start):
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]
    for _ in range(n - 1):
        now = get_smallest_node()
        visited[now] = True
        for i in graph[now]:
            if distance[i[0]] > (distance[now] + i[1]):
                distance[i[0]] = distance[now] + i[1]


dijkstra(start)

for i in range(1, n + 1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])
