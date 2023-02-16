W, H, N = map(int, input().split())
W_flag = [True] * W
H_flag = [True] * H
points = []

for _ in range(N):
    x, y, a = map(int, input().split())
    if a == 1 and x > 0:
        W_flag[:x] = [False] * x
    elif a == 2 and x < W:
        W_flag[x:] = [False] * (W - x)
    elif a == 3 and y > 0:
        H_flag[:y] = [False] * y
    elif a == 4 and y < H:
        H_flag[y:] = [False] * (H - y)

print(sum(W_flag) * sum(H_flag))
