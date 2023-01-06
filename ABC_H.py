N = int(input())

D = [int(input()) for _ in range(N)]

for i in range(N-1):
    max_index = i
    for j in range(i+1, N):
        if D[max_index] < D[j]:
            max_index = j
    temp = D[i]
    D[i] = D[max_index]
    D[max_index] = temp

unique_D = []

for d in D:
    if d not in unique_D:
        unique_D.append(d)

print(len(unique_D))