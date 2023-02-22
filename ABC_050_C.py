N = int(input())
A = list(map(int, input().split()))

cnt = [0] * (N+1)

for a in A:
    cnt[a] += 1

if N % 2 == 0:
    for i in range(1, N, 2):
        if cnt[i] != 2:
            print(0)
            exit()
else:
    if cnt[0] != 1:
        ans = 0
    for i in range(2, N, 2):
        if cnt[i] != 2:
            print(0)
            exit()

print(2 ** (N // 2) % (10 ** 9 + 7))