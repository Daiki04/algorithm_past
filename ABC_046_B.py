N, K = map(int, input().split())

dp = [[0] * K for _ in range(N)]

for i in range(K):
    dp[0][i] = 1

for i in range(1, N):
    for j in range(K):
        for k in range(K):
            if j != k:
                dp[i][j] += dp[i - 1][k]
print(sum(dp[-1]))