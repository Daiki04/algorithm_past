N, K = map(int, input().split())
D = list(map(int, input().split()))
A = [i for i in range(10) if i not in D]

while True:
    flag = True
    for i in str(N):
        if int(i) not in A:
            flag = False
            break
    if flag:
        print(N)
        break
    N += 1