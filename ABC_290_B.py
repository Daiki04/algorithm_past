N, K = map(int, input().split())
S = list(input())
ans = ["x"] * N

ct = 0

for i in range(N):
    if S[i] == "o":
        ans[i] = "o"
        ct += 1
    
    if ct == K:
        break

print("".join(ans))