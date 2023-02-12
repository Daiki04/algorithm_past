T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    C = list(map(int, input().split()))
    G = [[] for _ in range(N)]
    for _ in range(M):
        aoki = []
        takahashi = []
        ans = 0
        a, b = map(int, input().split())
        G[a-1].append(b-1)
        G[b-1].append(a-1)

        flag = [False] * N
