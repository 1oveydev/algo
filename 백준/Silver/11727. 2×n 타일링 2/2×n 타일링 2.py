# 백준 11727 2*n 타일링 - 2

import sys
input = sys.stdin.readline
n = int(input())
dp = [0 for _ in range(1001)]
dp[1] , dp[2] = 1, 3

for i in range(3,n+1):
    dp[i] = dp[i-1] + 2 * dp[i-2]

print(dp[n] % 10007)


