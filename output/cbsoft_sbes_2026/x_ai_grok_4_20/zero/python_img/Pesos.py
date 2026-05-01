
import sys

input = sys.stdin.read
data = input().split()

N = int(data[0])
weights = list(map(int, data[1:]))

if N == 0:
    print("S")
    sys.exit()

max_weight = weights[-1]

possible = True
for w in weights:
    if w > max_weight + 8:
        possible = False
        break

if not possible:
    print("N")
    sys.exit()

left = 0
right = N - 1
while left < right:
    if weights[right] - weights[left] > 8:
        possible = False
        break
    left += 1
    right -= 1

if possible:
    print("S")
else:
    print("N")
