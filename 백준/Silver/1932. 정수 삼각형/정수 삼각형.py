import sys
n = int(input())
dp = []
for i in range(n):
  dp.append(list(map(int, input().split())))
for i in range(2,n+1):
  for j in range(i):
    if j == 0:
      dp[i-1][j] += dp[i-2][j]
    elif j == i-1:
      dp[i-1][j] += dp[i-2][j-1]
    else:
      dp[i-1][j] += max(dp[i-2][j-1], dp[i-2][j])
print(max(dp[n-1]))