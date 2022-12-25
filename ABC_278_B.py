H, M = input().split()
H = [int(i) for i in list(H.zfill(2))]
M = [int(i) for i in list(M.zfill(2))]

if H[1] > 5:
    H[0] = (H[0]+1) % 3
    H[1] = 0
    M = [0, 0]
else:
    if H[0] == 2:
        if M[0] > 3:
            H[1] += 1
            H[0] = (H[0] + H[1]//10) % 3
            H[1] = H[1] % 10
            M = [0, 0]

print(10*H[0]+H[1], 10*M[0]+M[1])