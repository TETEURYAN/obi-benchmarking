import sys
data = sys.stdin.read().split()
E = int(data[0])
D = int(data[1])
if E > D:
    print(E + D)
else:
    print(2 * (D - E))