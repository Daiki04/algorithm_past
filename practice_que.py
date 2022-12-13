from collections import deque

# 頂点の数N，辺情報（隣接リスト）E，始点情報Sは定義済みとする
N = 0
E = []
S = 0

visited = [False] * N

Q = deque()
Q.append(S)
visited[S] = True

while len(Q) > 0:
    i = Q.popleft()
    for j in E[i]:
        visited[j] = True
        Q.append(j)