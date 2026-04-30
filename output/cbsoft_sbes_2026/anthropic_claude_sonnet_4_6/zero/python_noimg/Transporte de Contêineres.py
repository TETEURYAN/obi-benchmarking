A, B, C = map(int, input().split())
X, Y, Z = map(int, input().split())

if C > Z:
    print(0)
else:
    cols = X // A
    rows = Y // B
    layers = Z // C
    print(cols * rows * layers)