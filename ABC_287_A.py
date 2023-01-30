N = int(input())

ans = [False] * N

for i in range(N):
    s = input()
    if s == "For":
        ans[i] = True

print("Yes" if sum(ans) >= (N // 2+1) else "No")