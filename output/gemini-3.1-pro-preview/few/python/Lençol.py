import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

A1, B1, A2, B2, A, B = map(int, input_data)

P1 = [(A1, B1), (B1, A1)]
P2 = [(A2, B2), (B2, A2)]
T = [(A, B), (B, A)]

possible = False

for w1, h1 in P1:
    for W, H in T:
        if w1 >= W and h1 >= H:
            possible = True

for w2, h2 in P2:
    for W, H in T:
        if w2 >= W and h2 >= H:
            possible = True

for w1, h1 in P1:
    for w2, h2 in P2:
        for W, H in T:
            if w1 >= W and w2 >= W and h1 + h2 >= H:
                possible = True

if possible:
    print("S")
else:
    print("N")