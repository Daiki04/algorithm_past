import itertools

S = list(input())
ans = 0

for i in range(2**len(S)):
    tmp = 0
    p = 0
    for j in range(len(S)):
        if i & (1 << j):
            tmp += int("".join(S[p:j+1]))
            p = j+1
    ans += tmp
    print(tmp)
print(ans)
        