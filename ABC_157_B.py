A = [list(map(int, input().split()))for _ in range(3)]
N = int(input())
B = [int(input()) for _ in range(N)]

bingo = [[False]*3 for _ in range(3)]
flag = False

for b in B:
    for i in range(3):
        if b in A[i]:
            for j in range(3):
                if A[i][j] == b:
                    bingo[i][j] = True

for i in range(3):
    if bingo[i][0] and bingo[i][1] and bingo[i][2]:
        flag = True

for i in range(3):
    if bingo[0][i] and bingo[1][i] and bingo[2][i]:
        flag = True

if bingo[0][0] and bingo[1][1] and bingo[2][2]:
    flag = True

if bingo[0][2] and bingo[1][1] and bingo[2][0]:
    flag = True

if flag:
    print("Yes")
else:
    print("No")