N, K = map(int, input().split())
counts = [0] * (26)

for _ in range(N):
    s = set(input())
    for i in s:
        counts[ord(i)-ord("a")] += 1

ans = 0
for c in counts:
    if c == K:
        ans += 1
print(ans)