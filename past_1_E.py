N, Q = map(int, input().split())

graph = [[set(), set()] for _ in range(N)]

Query = [list(map(int, input().split())) for _ in range(Q)]

for query in Query:
    if query[0] == 1:
        graph[query[1]-1][0].add(query[2]-1)
        graph[query[2]-1][1].add(query[1]-1)
    elif query[0] == 2:
        graph[query[1]-1][0] = graph[query[1]-1][0] | graph[query[1]-1][1]
        for i in graph[query[1]-1][1]:
            graph[i][1].add(query[1]-1)
    else:
        f_u = graph[query[1]-1][0].copy()
        for i in f_u:
            if i == (query[1]-1):
                continue
            graph[query[1]-1][0] = graph[query[1]-1][0] | graph[i][0]
            for j in graph[i][0]:
                graph[j][1].add(query[1]-1)

for i in range(len(graph)):
    l = ["N"] * N
    for j in graph[i][0]:
        if i == j:
            continue
        l[j] = "Y"

    print("".join(l))
