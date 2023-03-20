H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
base = ord("A")

for i in range(H):
    for j in range(W):
        if A[i][j] == 0:
            print(".", end = "")
        else:
            print(chr(base + (A[i][j] - 1)), end = "")
    print()
