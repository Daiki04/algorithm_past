S = list(input())
num = [str(i) for i in range(10)]
flag = False

if len(S) == 8:
    if (S[0] not in num) and (S[7] not in num) and (S[1] != "0"):
        for i in range(1, 7):
            if S[i] not in num:
                break
            if i == 6:
                flag = True
if flag:
    print("Yes")
else:
    print("No")