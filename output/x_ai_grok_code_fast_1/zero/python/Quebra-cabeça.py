
import sys

input = sys.stdin.read
data = input().split()

N = int(data[0])
pieces = {}
index = 1
for _ in range(N):
    E = int(data[index])
    C = data[index + 1]
    D = int(data[index + 2])
    pieces[E] = (C, D)
    index += 3

result = []
current_E = 0
while True:
    C, D = pieces[current_E]
    result.append(C)
    if D == 1:
        break
    current_E = D

print(''.join(result))
