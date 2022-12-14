import sys
sys.setrecursionlimit(1000000)

# 頂点の数N，辺情報（隣接リスト）E，始点情報Sは定義済みとする
N = 0
E = []
S = 0

visited = [False] * N

def dfs(i):
    visited[i] = True
    for j in E[i]:
        if not visited[j]:
            dfs(j)

dfs(s)