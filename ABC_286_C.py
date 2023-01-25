N, A, B = map(int, input().split())
S = input()
ans = float("INF")

for i in range(N):
    cnt = 0
    for j in range(N//2):
        if S[j] != S[-j-1]:
            cnt += 1
    ans = min(ans, A*i + B*cnt)
    S = S[1:] + S[0]
print(ans)