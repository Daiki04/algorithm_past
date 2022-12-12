N, M, Q = map(int, input().split())

graph = [[] for _ in range(N)]

for _ in range(M):
    u, v = map(int, input().split())
    graph[u-1].append(v-1)
    graph[v-1].append(u-1)

color = list(map(int, input().split()))
Query = []

for _ in range(Q):
    q = list(map(int, input().split()))
    Query.append(q)

for query in Query:
    if query[0] == 1:
        print(color[query[1]-1])
        for i in graph[query[1]-1]:
            color[i] = color[query[1]-1]
    else:
        print(color[query[1]-1])
        color[query[1]-1] = query[2]