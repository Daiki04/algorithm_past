S = list(input())
base = ord("A")
ans = 0

p = len(S)
for i in S:
    delta = ord(i) - base + 1
    ans += delta * (26 ** (p-1))
    p -= 1
print(ans)
