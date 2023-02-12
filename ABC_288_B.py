N, K = map(int, input().split())
S = [input() for _ in range(N)]
S = S[:K]
S.sort()

for i in range(K):
    print(S[i])