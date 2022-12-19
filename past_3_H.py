N, L = map(int, input().split())
x = list(map(int, input().split()))
T = list(map(int, input().split()))

a1 = T[0]
a2 = T[0] + T[1]
a3 = T[0] + 3 * T[1]

A = [10**100] * (L+1)
A[0] = 0
A[1] = a1

for i in range(2, L+1):
    A[i] = min(A[i], A[i-1] + a1)
    if i >= 2:
        A[i] = min(A[i], A[i-2] + a2)
    if i >= 4:
        A[i] = min(A[i], A[i-4] + a3)
    if i in x:
        A[i] += T[2]

ans = A[L]

for i in [L-3, L-2, L-1]:
    if i >= 0:
        ans = min(ans, A[i] + T[0]//2 + T[1]*(2*(L-i)-1)//2)
print(ans)
