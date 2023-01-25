N, P, Q, R, S = map(int, input().split())
A = list(map(int, input().split()))
B = A.copy()

temp = A[P-1: Q].copy()
B[P-1: Q] = A[R-1: S].copy()
B[R-1: S] = temp.copy()

print(*B)