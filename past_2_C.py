N = int(input())
S = [list(input()) for _ in range(N)]

for i in range(N-2, -1, -1):
    start = (N-1) - i
    end = ((2*N-1) - 2*start) + start
    for j in range(start, end):
        if S[i+1][j-1] == "X" or S[i+1][j] == "X" or S[i+1][j+1] == "X":
            S[i][j] = "X"

for i in range(len(S)):
    s = "".join(S[i])
    print(s)