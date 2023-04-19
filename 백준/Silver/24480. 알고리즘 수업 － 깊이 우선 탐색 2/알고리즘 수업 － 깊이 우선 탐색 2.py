import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m, r = map(int, input().split())
graph = [[] for _ in range(n+1)]
cnt = [0]*(n+1)
tmp = 1
for _ in range(m):
  u, v = map(int, input().split())
  graph[u].append(v)
  graph[v].append(u)
for i in range(n+1):
  graph[i].sort(reverse=True)
def dfs(v):
  global tmp
  cnt[v] = tmp
  for w in graph[v]:
    if cnt[w] == 0:
      tmp += 1
      dfs(w)
dfs(r)
for i in range(1, n+1):
  print(cnt[i])