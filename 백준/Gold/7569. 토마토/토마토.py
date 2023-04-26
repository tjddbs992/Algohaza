# 백준 7569번 토마토
from collections import deque
m, n, h = map(int, input().split())
graph = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
tmp = []
q = deque()

for i in range(h):
  for j in range(n):
    for k in range(m):
      if graph[i][j][k] == 1:
        q.append((k, j, i))

def bfs():
  dx = [0, 0, -1, 1, 0, 0]
  dy = [1, -1, 0, 0, 0, 0]
  dz = [0, 0, 0, 0, -1, 1]
  while q:
    x, y, z = q.popleft()
    for i in range(6):
      nx = x + dx[i]
      ny = y + dy[i]
      nz = z + dz[i]
      if 0 <= nx < m and 0 <= ny < n and 0 <= nz < h and graph[nz][ny][nx] == 0:
        graph[nz][ny][nx] = graph[z][y][x] + 1
        q.append((nx, ny, nz))

bfs()
ans = 0
for i in graph:
  for j in i:
    for k in j:
      if k == 0:
        print(-1)
        exit(0)
    ans = max(ans, max(j))
print(ans - 1)