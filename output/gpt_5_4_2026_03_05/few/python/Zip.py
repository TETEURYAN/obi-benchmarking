import sys

data = list(map(int, sys.stdin.read().split()))
l1, l2, c1, c2 = data

def score(a, b):
    s = a + b
    if a == b:
        return 2 * s
    if abs(a - b) == 1:
        return 3 * s
    return s

sl = score(l1, l2)
sc = score(c1, c2)

if sl > sc:
    print("Lia")
elif sc > sl:
    print("Carolina")
else:
    print("empate")