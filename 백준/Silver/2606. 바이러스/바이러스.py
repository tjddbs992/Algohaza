n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
discovered = []
for _ in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)
def dfs(v, discovered=[]):
  discovered.append(v)
  for w in graph[v]:
    if w not in discovered:
      discovered = dfs(w, discovered)
  return discovered
dfs(1, discovered)
print(len(discovered) - 1)