
import sys

input = sys.stdin.read
data = input().split()

N = int(data[0])
H = [int(x) for x in data[1:]]

if N == 0:
    print(0)
    sys.exit()

max_h = max(H)
count = 0

for level in range(1, max_h + 1):
    i = 0
    while i < N:
        if H[i] >= level:
            i += 1
            continue
        j = i
        while j < N and H[j] < level:
            j += 1
        left = i - 1
        right = j
        has_left = left >= 0 and H[left] >= level
        has_right = right < N and H[right] >= level
        if has_left and has_right:
            count += (j - i)
        i = j

print(count)
