import sys

input_data = sys.stdin.read().split()
P1 = int(input_data[0])
C1 = int(input_data[1])
P2 = int(input_data[2])
C2 = int(input_data[3])

if P1 * C1 == P2 * C2:
    print(0)
elif P1 * C1 > P2 * C2:
    print(-1)
else:
    print(1)