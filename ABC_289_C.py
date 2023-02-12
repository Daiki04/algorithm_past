N, M = map(int, input().split())
S = []
for _ in range(M):
    C = int(input())
    S.append(set(list(map(int, input().split()))))

all_set = set([i for i in range(1, N+1)])
ans = 0

for i in range(2 ** M):
    temp = set()
    for j in range(M):
        if (i >> j) & 1:
            temp = temp | S[j]
    if temp == all_set:
        ans += 1
print(ans)
