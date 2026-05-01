import sys

data = sys.stdin.read().split()
X = int(data[0])
for i in range(1, len(data)):
    T = int(data[i])
    if T > X:
        print("menor")
    elif T < X:
        print("maior")
    else:
        print("correto")