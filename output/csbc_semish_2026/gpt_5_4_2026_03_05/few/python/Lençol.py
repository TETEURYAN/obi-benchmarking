import sys

data = list(map(int, sys.stdin.read().split()))
a1, b1, a2, b2, A, B = data

def fits(x, y, w, h):
    return x >= w and y >= h

def possible(W, H):
    rects = [(a1, b1), (b1, a1)]
    rects2 = [(a2, b2), (b2, a2)]
    for x1, y1 in rects:
        for x2, y2 in rects2:
            if y1 == H and y2 == H and x1 + x2 >= W:
                return True
            if x1 == W and x2 == W and y1 + y2 >= H:
                return True
    return False

if possible(A, B) or possible(B, A):
    print("S")
else:
    print("N")