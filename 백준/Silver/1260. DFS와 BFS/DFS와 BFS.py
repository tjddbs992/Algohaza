import sys
input = sys.stdin.readline
n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]
disc1 = []
disc2 = []
for _ in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)
for i in range(n+1):
  graph[i].sort()
def dfs(v, discovered=[]):
  discovered.append(v)
  for w in graph[v]:
    if w not in discovered:
      discovered = dfs(w, discovered)
  return discovered
def bfs(v, discovered=[]):
  queue = [v]
  cnt = 0
  while queue:
    if cnt == 0:
      discovered.append(v)
    v = queue.pop(0)
    cnt += 1
    for w in graph[v]:
      if w not in discovered:
        queue.append(w)
        discovered.append(w)
  return discovered
dfs(v, disc1)
bfs(v, disc2)
print(*disc1)
print(*disc2)