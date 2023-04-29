from collections import deque

n, m = map(int, input().split())
graph = [0] * 101
visited = [0] * 101
ladder = dict()
snake = dict()

for _ in range(n):
  a, b = map(int, input().split())
  ladder[a] = b
for _ in range(m):
  a, b = map(int, input().split())
  snake[a] = b

def bfs():
  q = deque()
  q.append(1)
  while q:
    x = q.popleft()
    if x == 100:
      print(graph[x])
      return
    for i in range(1, 7):
      next = x + i
      if next <= 100 and visited[next] == 0:
        if next in ladder.keys():
          next = ladder[next]
        if next in snake.keys():
          next = snake[next]
        if visited[next] == 0:
          visited[next] = 1
          graph[next] = graph[x] + 1
          q.append(next)
bfs()