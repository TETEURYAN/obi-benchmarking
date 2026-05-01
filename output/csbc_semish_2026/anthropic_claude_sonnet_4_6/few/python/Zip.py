import sys

data = sys.stdin.read().split()
a, b, c, d = int(data[0]), int(data[1]), int(data[2]), int(data[3])

def score(x, y):
    s = x + y
    if x == y:
        return 2 * s
    elif abs(x - y) == 1:
        return 3 * s
    else:
        return s

sl = score(a, b)
sc = score(c, d)

if sl > sc:
    print("Lia")
elif sc > sl:
    print("Carolina")
else:
    print("empate")