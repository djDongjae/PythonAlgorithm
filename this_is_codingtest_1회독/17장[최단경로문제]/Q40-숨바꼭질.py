import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
distance = [[INF] * (n+1)]
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = 