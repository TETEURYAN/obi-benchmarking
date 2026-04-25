import sys

data = sys.stdin.read().split()
N = int(data[0])
pieces = {}
idx = 1
for i in range(N):
    E = int(data[idx])
    C = data[idx + 1]
    D = int(data[idx + 2])
    pieces[E] = (C, D)
    idx += 3

current_E = 0
result = []
while True:
    C, D = pieces[current_E]
    result.append(C)
    if D == 1:
        break
    current_E = D
print(''.join(result))