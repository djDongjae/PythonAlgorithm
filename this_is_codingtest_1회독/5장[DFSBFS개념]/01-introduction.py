def recursive_function():
  print('재귀 함수를 호출합니다.')
  recursive_function()

recursive_function()

def recursive_function(i):
  if i == 100:
    return
  print(i, '번째 재귀 함수에서', i + 1, '번째 재귀 함수를 호출합니다.')
  recursive_function(i + 1)
  print(i, '번째 재귀 함수를 종료합니다.')


recursive_function(10)

def factorial_iterative(n):
  result = 1
  for i in range(1, n+1):
    result *= i
  return result

def factorial_recursive(n):
  if n <= 1:
    return 1
  return n * factorial_recursive(n-1)

print('반복적으로 구현:', factorial_iterative(5))
print('재귀적으로 구현:', factorial_recursive(5))

INF = 999999999

graph = [
         [0, 7, 5],
         [7, 0, INF],
         [5, INF, 0]
]

print(graph)
graph = [[] for _ in range(3)]

graph[0].append((1, 7))
graph[0].append((2, 5))

graph[1].append((0, 7))

graph[2].append((0, 5))

print(graph)

def dfs(graph, v, visited):
  visited[v] = True
  print(v, end=' ')
  for i in graph[v]:
    if not visited[i]:
      dfs(graph, i, visited)

graph = [
         [],
         [2, 3, 8],
         [1, 7],
         [1, 4, 5],
         [3, 5],
         [3, 4],
         [7],
         [2, 6, 8],
         [1, 7]
]

visited = [False]*9
dfs(graph, 1, visited)

from collections import deque

def bfs(graph, start, visited):
  queue = deque([start])
  visited[start] = True
  while queue:
    v = queue.popleft()
    print(v, end=' ')
    for i in graph[v]:
      if not visited[i]:
        visited[i] = True
        queue.append(i)

graph = [
         [],
         [2, 3, 8],
         [1, 7],
         [1, 4, 5],
         [3, 5],
         [3, 4],
         [7],
         [2, 6, 8],
         [1, 7]
]

visited = [False] * 9

bfs(graph, 1, visited)
