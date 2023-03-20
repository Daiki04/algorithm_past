N, M = map(int, input().split())

G = [[] for _ in range(N)]
visited = [False] * N
edges = [0] * N

for _ in range(M):
    u, v = map(int, input().split())
    G[u-1].append(v-1)
    G[v-1].append(u-1)
    edges[u-1] += 1
    edges[v-1] += 1
    if u == v:
        visited[u-1] = True

def dfs(v, last):
    global edge_count
    global point_count
    visited[v] = True
    point_count += 1
    for u in G[v]:
        if u != last:
            edge_count += 1
        if not visited[u]:
            dfs(u, v)

for i in range(N):
    edge_count = 0
    point_count = 0
    if not visited[i]:
        dfs(i, -1)
        if edge_count != point_count:
            print('No')
            print(edge_count, point_count)
            exit()

print('Yes')