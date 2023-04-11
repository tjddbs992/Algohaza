import sys
input = sys.stdin.readline
n = int(input())
p = []
for i in range(n):
  p.append(int(input()))
dp = []
for i in range(n):
  if i == 0:
    dp.append(p[i])
  elif i == 1:
    dp.append(p[i-1] + p[i])
  elif i == 2:
    dp.append(max(p[i-2] + p[i], p[i-1] + p[i]))
  else:
    dp.append(max(dp[i-2] + p[i], dp[i-3] + p[i-1] + p[i]))
print(dp[n-1])