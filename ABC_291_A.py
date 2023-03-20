S = input()

L = [chr(i+ord("A")) for i in range(26)]

for i in  range(len(S)):
    if S[i] in L:
        print(i+1)
        exit()