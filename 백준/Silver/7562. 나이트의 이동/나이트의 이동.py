from collections import deque

def bfs(x, y):
  dx = [-2, -1, 1, 2, -2, -1, 1, 2]
  dy = [1, 2, 2, 1, -1, -2, -2, -1]
  q = deque()
  q.append((x, y))
  while q:
    x, y = q.popleft()
    if (x, y) == (a, b):
      return graph[x][y]
    for i in range(8):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 0:
        graph[nx][ny] = graph[x][y] + 1
        q.append((nx, ny))
  
t = int(input())
for _ in range(t):
  n = int(input())
  graph = [[0]*n for _ in range(n)]
  x, y = map(int, input().split())
  a, b = map(int, input().split())
  print(bfs(x, y))