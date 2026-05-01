import sys

data = sys.stdin.read().split()
N1, D1, V1 = int(data[0]), int(data[1]), int(data[2])
N2, D2, V2 = int(data[3]), int(data[4]), int(data[5])
if D1 * V2 < D2 * V1:
    print(N1)
else:
    print(N2)