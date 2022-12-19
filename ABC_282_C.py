N = int(input())
S = input().split('"')

for i in range(0, len(S), 2):
    S[i] = S[i].replace(",", ".")
print('"'.join(S))