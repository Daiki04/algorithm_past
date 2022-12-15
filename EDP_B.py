N, K = map(int, input().split())
h = list(map(int, input().split()))

cost = [0] * N
cost[0] = 0

for i in range(1, K+1):
    min_i = cost[i-1] + abs(h[i-1] - h[i])
    for j in range(1, i+1):
        min_i = min(min_i, cost[i-j] + abs(h[i-j] - h[i]))
    cost[i] = min_i

for i in range(K+1, N):
    min_i = cost[i-1] + abs(h[i-1] - h[i])
    for j in range(1, K+1):
        min_i = min(min_i, cost[i-j] + abs(h[i-j] - h[i]))

print(cost[N-1])