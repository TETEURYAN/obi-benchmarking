A, B, C = map(int, input().split())
X, Y, Z = map(int, input().split())

if C > Z:
    print(0)
else:
    layers = Z // C
    per_layer = (X // A) * (Y // B)
    print(layers * per_layer)