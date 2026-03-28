import sys
import math

def cabe(a, b, p, q):
    if a <= p and b <= q:
        return True
    if b <= p and a <= q:
        return True
    denom = a * p - b * q
    if denom == 0:
        return False
    t = (a * q - b * p) / denom
    if t < 0:
        return False
    cos_theta = 1 / math.sqrt(1 + t * t)
    sin_theta = t / math.sqrt(1 + t * t)
    x = a * cos_theta + b * sin_theta
    y = a * sin_theta + b * cos_theta
    return x <= p + 1e-9 and y <= q + 1e-9

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    A = int(data[0])
    B = int(data[1])
    C = int(data[2])
    H = int(data[3])
    L = int(data[4])
    pares = [(A, B), (A, C), (B, C)]
    for a, b in pares:
        if cabe(a, b, H, L) or cabe(a, b, L, H):
            print('S')
            return
    print('N')

if __name__ == "__main__":
    main()