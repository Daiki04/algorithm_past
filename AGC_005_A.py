from collections import deque

X = list(input())

q = deque()
q.append(X[0])

for i in range(1, len(X)):
    if len(q) != 0 and q[-1] == "S" and X[i] == "T":
        q.pop()
    else:
        q.append(X[i])

print(len(q))