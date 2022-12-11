C = [list(map(int, input().split())) for _ in range(3)]

flag = True

if (C[0][0]-C[0][1] != C[1][0]-C[1][1]) or (C[1][0]-C[1][1] != C[2][0]-C[2][1]):
    flag = False

if (C[0][1]-C[0][2] != C[1][1]-C[1][2]) or (C[1][1]-C[1][2] != C[2][1]-C[2][2]):
    flag = False

if (C[0][0]-C[1][0] != C[0][1]-C[1][1]) or (C[0][1]-C[1][1] != C[0][2]-C[1][2]):
    flag = False

if (C[1][0]-C[2][0] != C[1][1]-C[2][1]) or (C[1][1]-C[2][1] != C[1][2]-C[2][2]):
    flag = False


if flag:
    print("Yes")
else:
    print("No")