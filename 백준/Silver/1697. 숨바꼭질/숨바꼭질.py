import sys
from collections import deque
input = sys.stdin.readline

def bfs(x):
  queue = deque()
  queue.append(x)
  while queue:
    x = queue.popleft()
    if x == k:
      return graph[x]
    for nx in (x-1, x+1, x*2):
      if 0 <= nx < MAX and graph[nx] == 0:
        graph[nx] = graph[x] + 1
        queue.append(nx)
        
n, k = map(int, input().split())
MAX = 100001
graph = [0]*MAX
print(bfs(n))