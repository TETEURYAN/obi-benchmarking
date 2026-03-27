
import sys

input = sys.stdin.read
data = input().split()

N = int(data[0])
X1 = int(data[1])
Y1 = int(data[2])
X2 = int(data[3])
Y2 = int(data[4])

M = N // 2

horiz = (X1 <= M and X2 > M) or (X1 > M and X2 <= M)
vert = (Y1 <= M and Y2 > M) or (Y1 > M and Y2 <= M)

if horiz or vert:
    print("S")
else:
    print("N")
