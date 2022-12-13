N = int(input())
stocks = list(map(int, input().split()))
Q = int(input())
Query = [list(map(int, input().split())) for _ in range(Q)]
sum = 0
set_odd = (N//2) + (N%2)
ans = 0
s = 0
z = 0

min_s = 10**10
min_z = 10**10

for i in range(N):
    if i % 2 == 0:
        min_s = min(min_s, stocks[i])
    else:
        min_z = min(min_z, stocks[i])

for query in Query:
    if query[0] == 1:
        index = query[1] - 1
        sell = query[2]

        if index%2 == 0:
            card_x = stocks[index] - z - s
        else:
            card_x = stocks[index] - z

        if card_x >= sell:
            stocks[index] -= sell
            ans += sell

            if index%2 == 0:
                min_s = min(min_s, stocks[index])
            else:
                min_z = min(min_z, stocks[index])
    elif query[0] == 2:
        sell = query[1]

        if min_s - s - z >= sell:
            s += sell
    else:
        sell = query[1]

        if min(min_z - z, min_s - z - s) >= sell:
            z += sell

ans += set_odd*s + N*z
print(ans)