S = list(input())

oomoji = [chr(ord("A")+i) for i in range(26)]
komoji = [chr(ord("a")+i) for i in range(26)]
set_S = set(S)

flags = [False] * 3

for i in S:
    if i in oomoji:
        flags[0] = True
    if i in komoji:
        flags[1] = True

if len(set_S) == len(S):
    flags[2] = True

print("Yes" if sum(flags)==3 else "No")