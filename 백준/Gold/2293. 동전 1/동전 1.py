import sys
input = sys.stdin.readline
n, k = map(int, input().split())
dp = [0]*(k+1)
dp[0] = 1
for i in range(n):
  v = int(input())
  for j in range(v, k+1):
    dp[j] += dp[j-v]
print(dp[k])