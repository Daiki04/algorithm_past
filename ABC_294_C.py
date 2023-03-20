N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = A + B
C.sort()

rank_A = []
rank_B = []

for i in range(N + M):
    if C[i] in A:
        rank_A.append(i + 1)
    else:
        rank_B.append(i + 1)

print(*rank_A)
print(*rank_B)