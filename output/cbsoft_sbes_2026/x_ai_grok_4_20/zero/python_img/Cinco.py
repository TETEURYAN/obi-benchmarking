
import sys

input = sys.stdin.read
data = input().split()

N = int(data[0])
digits = list(map(int, data[1:]))

# Find positions of all 0 and 5
positions = {0: [], 5: []}
for i in range(N):
    d = digits[i]
    if d == 0 or d == 5:
        positions[d].append(i)

# To get the largest number, we want to change as little as possible from the left
# We will try all possible swaps that make last digit 0 or 5, and choose the one that gives largest number

best = None
best_num = None

for target in [0, 5]:
    if not positions[target]:
        continue
    for j in positions[target]:  # j is the position we will put at the end
        for i in range(N):
            if i == j:
                continue
            # swap i and j
            new_digits = digits[:]
            new_digits[i], new_digits[j] = new_digits[j], new_digits[i]
            # now last digit is target, so divisible by 5
            # compare
            if best is None or new_digits > best:
                best = new_digits[:]
                best_num = new_digits

if best is None:
    print(-1)
else:
    print(' '.join(map(str, best)))
