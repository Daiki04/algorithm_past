N, A, B = map(int, input().split())
ans = 0

for i in range(N+1):
    t = sum(list(map(int, list(str(i)))))
    if A <= t <= B:
        ans += i

print(ans)
