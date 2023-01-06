N = int(input())
A = list(map(int, input().split()))
alice = 0
bob = 0

for i in range(N-1):
    max_index = i
    for j in range(i+1, N):
        if A[max_index] < A[j]:
            max_index = j
    temp = A[i]
    A[i] = A[max_index]
    A[max_index] = temp

for i in range(N):
    if i % 2 == 0:
        alice += A[i]
    else:
        bob += A[i]

print(alice - bob)