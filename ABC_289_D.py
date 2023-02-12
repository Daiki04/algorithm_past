N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))
X = int(input())

G = [0] * (X+1)
G[0] = 1

for b in B:
    G[b] = -1

for i in range(X+1):
    if G[i] > 0:
        for j in range(N):
            if i + A[j] <= X and G[i + A[j]] != -1:
                G[i + A[j]] = 1

print("Yes" if G[-1] == 1 else "No")