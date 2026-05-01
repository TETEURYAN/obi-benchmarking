
import sys

input = sys.stdin.read
data = input().split()

N = int(data[0])
weights = list(map(int, data[1:]))

if N == 0:
    print("S")
    sys.exit()

weights.sort(reverse=True)
max_w = weights[0]

if max_w > 16:
    print("N")
    sys.exit()

total = sum(weights)
if total % 2 != 0:
    print("N")
    sys.exit()

target = total // 2

possible = [False] * (target + 1)
possible[0] = True

for w in weights:
    for j in range(target, w - 1, -1):
        if possible[j - w]:
            possible[j] = True

if not possible[target]:
    print("N")
    sys.exit()

print("S")
