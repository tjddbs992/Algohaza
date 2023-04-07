import sys
n = int(input())
w = []
for i in range(n):
  w.append(int(input()))
if n == 1:
  dp = [w[0]]
elif n == 2:
  dp = [w[0], w[0] + w[1]]
else:
  dp = [w[0], w[0] + w[1], max(w[0]+w[1], w[0]+w[2], w[1]+w[2])]
  for i in range(3, n):
    dp.append(max(dp[i-1], dp[i-2] + w[i], dp[i-3] + w[i-1] + w[i]))
print(max(dp))