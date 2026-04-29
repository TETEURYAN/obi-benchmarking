import sys

data = list(map(int, sys.stdin.read().split()))
X, Y = data[0], data[1]
a, b = data[2], data[3]
c, d = data[4], data[5]

def cabe():
    for w1, h1 in ((a, b), (b, a)):
        for w2, h2 in ((c, d), (d, c)):
            if w1 <= X and h1 <= Y and w2 <= X and h2 <= Y:
                if max(h1, h2) <= Y and w1 + w2 <= X:
                    return True
                if max(w1, w2) <= X and h1 + h2 <= Y:
                    return True
    return False

print('S' if cabe() else 'N')