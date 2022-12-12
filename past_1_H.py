N = int(input())
stock = list(map(int, input().split()))
Q = int(input())
Query = [list(map(int, input().split())) for _ in range(Q)]
sum = 0
set_odd = (N//2) + (N%2)

for query in Query:
    if query[0] == 1:
        if stock[query[1]-1] - query[2] >= 0:
            stock[query[1]-1] -= query[2]
            sum += query[2]
    elif query[0] == 2:
        flag = True
        for i in range(0, N, 2):
            if stock[i] < query[1]:
                flag=False
                break
        
        if flag:
            for i in range(0, N, 2):
                stock[i] -= query[1]
            sum += query[1] * set_odd
    else:
        flag = True
        for i in range(0, N):
            if stock[i] < query[1]:
                flag=False
                break
        if flag:
            for i in range(0, N):
                stock[i] -= query[1]
            sum += query[1] * N

print(sum)
