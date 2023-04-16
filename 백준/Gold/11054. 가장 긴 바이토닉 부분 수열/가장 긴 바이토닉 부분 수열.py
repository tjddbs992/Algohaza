import sys
input = sys.stdin.readline
n = int(input())
a = [0] * n
dp = [1] * n
dp_d = [1] * n
len = [0] * n
a = list(map(int,input().split()))
for i in range(n):
  for j in range(i):
    if a[i] > a[j]:
      dp[i] = max(dp[i], dp[j]+1)
a.reverse()
for i in range(n):
  for j in range(i):
    if a[i] > a[j]:
      dp_d[i] = max(dp_d[i], dp_d[j] + 1)
dp_d.reverse()
for i in range(n):
  len[i] = dp[i] + dp_d[i]
print(max(len) - 1)