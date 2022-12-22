N = int(input())
p = list(map(int, input().split()))
TP = sum(p)

dp = [[False]*(TP+1) for _ in range(N+1)]

dp[0][0] = True

for i in range(N):
    for j in range(TP+1):
        if not dp[i][j]:
            continue
        dp[i+1][j] = True
        dp[i+1][j+p[i]] = True

print(sum(dp[N]))