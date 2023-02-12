N, M = map(int, input().split())
a = list(map(int, input().split()))

if M == 0:
    print(*[i for i in range(1, N+1)])
    exit()

G = [[] for _ in range(N)]

for c in a:
    G[c-1].append(c)
    G[c].append(c-1)

flag = [False] * N

def dfs(v):
    flag[v] = True
    for i in G[v]:
        if not flag[i]:
            dfs(i)
    print(v+1, end=" ")

for j in range(N):
    if not flag[j]:
        dfs(j)