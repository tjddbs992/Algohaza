import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
t = int(input())
cnt = 0
tmp = []

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def dfs(x, y):
  global cnt
  if x < 0 or x >= n or y < 0 or y >= m:
    return

  if graph[x][y] == 1:
    graph[x][y] = 0
    cnt += 1
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      dfs(nx, ny)
      
for i in range(t):
  m, n, k = map(int, input().split())
  graph = [[0]*m for _ in range(n)]
  for j in range(k):
    x, y = map(int, input().split())
    graph[y][x] = 1
    if j == k-1:
      for p in range(n):
        for q in range(m):
          if graph[p][q] == 1:
            dfs(p, q)
            tmp.append(cnt)
            cnt = 0
      print(len(tmp))
      tmp = []