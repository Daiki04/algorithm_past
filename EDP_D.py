N, W = map(int, input().split())
w = []
v = []

for _ in range(N):
    tw, tv = map(int, input().split())
    w.append(tw)
    v.append(tv)

dp = [[-1]*(W+1) for _ in range(N+1)]

dp[0][0] = 0

for i in range(N):
    for j in range(W+1):
        if dp[i][j] < 0:
            continue
            
        dp[i+1][j] = max(dp[i+1][j], dp[i][j])

        if j + w[i] <= W:
            dp[i+1][j+w[i]] = max(dp[i+1][j+w[i]], dp[i][j]+v[i])

print(max(dp[N]))