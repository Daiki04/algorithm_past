S = list(input())

ans = 1
last = S[0]

for i in range(1, len(S)):
    if last != S[i]:
        ans += 1
        last = S[i]

print(ans-1)