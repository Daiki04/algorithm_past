S = list(map(int, list(input())))

task = 1
counter = 0

for i in range(1, len(S)):
    if S[i] == 0:
        counter += 1
    elif S[i] != 0:
        task += 1
        if counter != 0:
            task += counter//2 + counter%2
            counter = 0
    if i == len(S)-1:
        task += counter//2 + counter%2
print(task)