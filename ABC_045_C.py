import itertools

S = list(input())
ans = 0

for i in range(1 << len(S)):
    tmp = 0
    s = 0
    for e in range(1, len(S)+1):
        if i & (1 << (e-1)):
            tmp += int("".join(S[s:e]))
            s = e
    if len(S[s:]) != 0:
        tmp += int("".join(S[s:]))
    ans += tmp

print(ans//2)