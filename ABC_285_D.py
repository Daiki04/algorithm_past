N = int(input())

S = []
T = []

for i in range(N):
    s, t = input().split()
    S.append(s)
    T.append(t)

unique_name = [i for i in range(N) if T[i] not in S]
flag = [False] * N
ans = "No"

while len(unique_name) > 0:
    for i in unique_name:
        S[i] = T[i]
        flag[i] = True
    next = [i for i in range(N) if T[i] not in S and flag[i] == False]
    if next == unique_name:
        break
    unique_name = next

if sum(flag) == N:
    ans = "Yes"

print(ans)

