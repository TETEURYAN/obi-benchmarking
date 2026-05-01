import sys

data = sys.stdin.read().split()
N = int(data[0])
A, B, C, D, E, F, G = int(data[1]), int(data[2]), int(data[3]), int(data[4]), int(data[5]), int(data[6]), int(data[7])

# By inclusion-exclusion:
# A + B + C - D - E - F - X + G = N
# where X is the number of people doing all three sports
# X = A + B + C - D - E - F + G - N

X = A + B + C - D - E - F + G - N

if X > 0:
    print("S")
else:
    print("N")