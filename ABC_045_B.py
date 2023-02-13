SA = list(input())
SB = list(input())
SC = list(input())

S = [SA, SB, SC]

turn = 0

while True:
    if len(S[turn]) == 0:
        print(chr(turn+65))
        break
    next = S[turn].pop(0)
    turn = ord(next)-97