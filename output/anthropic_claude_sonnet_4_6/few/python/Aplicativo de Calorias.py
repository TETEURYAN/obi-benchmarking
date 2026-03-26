import sys
data = sys.stdin.read().split()
E1 = int(data[0])
E2 = int(data[1])
E3 = int(data[2])
X = int(data[3])
print(E2 if E2 - E1 <= X else E3)