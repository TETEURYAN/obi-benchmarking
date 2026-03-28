import sys

data = sys.stdin.read().split()
idx = 0
N = int(data[idx])
idx += 1
M = int(data[idx])
idx += 1
A = set()
for i in range(N):
    A.add(int(data[idx]))
    idx += 1
B = []
for i in range(M):
    B.append(int(data[idx]))
    idx += 1
current_B = set()
for i in range(M):
    b = B[i]
    valid = False
    if b in A:
        valid = True
    else:
        for s in current_B:
            if b - s in current_B:
                valid = True
                break
    if not valid:
        print(b)
        sys.exit(0)
    current_B.add(b)
print("sim")