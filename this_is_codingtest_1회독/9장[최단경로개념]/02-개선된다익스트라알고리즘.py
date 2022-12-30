import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)
start = int(input())

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

