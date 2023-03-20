N = int(input())
S = list(input())

now = [0, 0]
G = set()
G.add((0, 0))

a = {
    "R": [1, 0],
    "L": [-1, 0],
    "U": [0, 1],
    "D": [0, -1]
}

for s in S:
    now[0] += a[s][0]
    now[1] += a[s][1]
    if (now[0], now[1]) in G:
        print("Yes")
        exit()
    G.add((now[0], now[1]))

print("No")