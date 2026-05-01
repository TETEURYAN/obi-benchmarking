import sys

input_data = sys.stdin.read().split()
A = int(input_data[0])
B = int(input_data[1])
C = int(input_data[2])
D = int(input_data[3])

diff1 = abs((A + B) - (C + D))
diff2 = abs((A + C) - (B + D))
diff3 = abs((A + D) - (B + C))

print(min(diff1, diff2, diff3))