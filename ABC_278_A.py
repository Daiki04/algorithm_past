from collections import deque

N, K = map(int, input().split())
A = list(map(int, input().split()))

q = deque()

for a in A:
    q.append(a)

for _ in range(K):
    q.popleft()
    q.append(0)

print(*q)
