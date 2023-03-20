N, Q = map(int, input().split())

counter = [0] * N

for _ in range(Q):
    l, r = map(int, input().split())
    if l == 1:
        counter[r-1] += 1
    elif l == 2:
        counter[r-1] += 2
    elif l == 3:
        if counter[r-1] >= 2:
            print('Yes')
        else:
            print('No')