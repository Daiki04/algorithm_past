import itertools

S = input()
T = input()
len_T = len(T)
len_S = len(S)


for x in range(len_T+1):
    end = len_T - x
    S_dash =  S[:x] + S[len_S-end:]
    T_dash = T
    while "?" in S_dash:
        S_dash = S_dash.replace("?", T_dash[S_dash.index("?")], 1)
    while "?" in T_dash:
        T_dash = T_dash.replace("?", S_dash[T_dash.index("?")], 1)
    
    if S_dash == T_dash:
        print("Yes")
    else:
        print("No")

    

