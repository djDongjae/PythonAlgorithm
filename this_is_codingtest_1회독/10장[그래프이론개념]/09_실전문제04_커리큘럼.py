from collections import deque
import copy

v = int(input())
graph = [[] for _ in range(v+1)]
indegree = [0] * (v+1)
time = [0] * (v+1)

for i in range(1, v+1):
    data = list(map(int, input().split()))
    time[i] = data[0]
    for x in data[1:-1]:
        indegree[i] += 1
        graph[x].append(i)


def topology_sort():
    result = copy.deepcopy(time)
    q = deque()

    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        for j in graph[now]:
            result[j] = max(result[j], result[now] + time[j])
            indegree[j] -= 1
            if indegree[j] == 0:
                q.append(j)

    for i in range(1, v+1):
        print(result[i])


topology_sort()