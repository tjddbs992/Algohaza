import sys
input = sys.stdin.readline
n, k = map(int, input().split())
dp = [0]*(k+1)
for i in range(n):
  v = int(input())
  for j in range(v, k+1):
    if j-v == 0:
      dp[j] += 1
    else:
      dp[j] += dp[j-v]
print(dp[k])