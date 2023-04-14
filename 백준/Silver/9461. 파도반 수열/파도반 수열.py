import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
  n = int(input())
  dp = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9]
  if n <= 10:
    print(dp[n-1])
  else:
    for i in range(10, n):
      dp.append(dp[i-2] + dp[i-3])
    print(dp[n-1])