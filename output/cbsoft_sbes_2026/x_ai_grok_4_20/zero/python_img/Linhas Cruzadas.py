
import sys

input = sys.stdin.read
data = input().split()

N = int(data[0])
P = list(map(int, data[1:]))

pos = [0] * (N + 1)
for i in range(N):
    pos[P[i]] = i

def merge_sort(arr):
    if len(arr) <= 1:
        return 0, arr
    mid = len(arr) // 2
    left_inv, left = merge_sort(arr[:mid])
    right_inv, right = merge_sort(arr[mid:])
    merge_inv, merged = merge(left, right)
    return left_inv + right_inv + merge_inv, merged

def merge(left, right):
    i = j = inv = 0
    merged = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            inv += len(left) - i
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return inv, merged

inv, _ = merge_sort(pos[1:])
print(inv)
