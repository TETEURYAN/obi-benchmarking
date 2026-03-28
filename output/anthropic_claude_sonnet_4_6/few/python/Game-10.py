import sys
data = sys.stdin.read().split()
N = int(data[0])
D = int(data[1])
A = int(data[2])
if D >= A:
    print(D - A)
else:
    print(N - A + D)