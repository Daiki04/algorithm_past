from collections import deque

N, M = map(int, input().split())
ans = [False] * N

G = [[] for _ in range(N)]

for _ in range(M):
    u, v = map(int, input().split())
    G[u-1].append(v-1)
    G[v-1].append(u-1)

Q = deque()
s = []

for i in range(N):
    if len(G[i]) == 1:
        s.append(i)
        break
if len(s) != 0:
    Q.append(s[0])

while len(Q) > 0:
    n = Q.pop()
    if len(G[n]) > 2:
        break
    for i in G[n]:
        if not ans[i]:
            ans[i] = True
            Q.append(i)

print("Yes" if sum(ans) == N else "No")
