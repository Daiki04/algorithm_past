N, X = map(int, input().split())
dp = [0] * (X+1)

dp[0] = 1

for i in range(N):
    a, b = map(int, input().split())
    for n in reversed(range(X+1)):
        for c in range(1, b+1):
            if 0 <= n - a*c and dp[n-c*a]:
                dp[n] = 1
print("Yes" if dp[X] else "No")
