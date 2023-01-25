N = int(input())
S = list(input())

for i in range(1, N):
    ans = 0
    for l in range(N):
        if i+l >= N or S[i+l] == S[l]:
            break
        if S[i+l] != S[l]:
            ans += 1
    print(ans)