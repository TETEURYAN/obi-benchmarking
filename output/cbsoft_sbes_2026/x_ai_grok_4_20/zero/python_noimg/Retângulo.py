
import sys

input = sys.stdin.read
data = input().split()

N = int(data[0])
L = list(map(int, data[1:]))

total = sum(L)
if total % 2 != 0:
    print("N")
    sys.exit()

half = total // 2

prefix = [0] * (2 * N + 1)
for i in range(2 * N):
    prefix[i + 1] = prefix[i] + L[i % N]

found = False
for i in range(N):
    target1 = prefix[i] + half
    target2 = prefix[i] + total // 2
    if target2 > prefix[i + N]:
        continue
    left = i + 1
    right = i + N
    while left <= right:
        mid = (left + right) // 2
        if prefix[mid] == target1:
            found = True
            break
        elif prefix[mid] < target1:
            left = mid + 1
        else:
            right = mid - 1
    if found:
        break
    left = i + 1
    right = i + N
    while left <= right:
        mid = (left + right) // 2
        if prefix[mid] == target2:
            found = True
            break
        elif prefix[mid] < target2:
            left = mid + 1
        else:
            right = mid - 1
    if found:
        break

if found:
    print("S")
else:
    print("N")
