import sys
sys.setrecursionlimit(200000)

data = sys.stdin.read().split()
N = int(data[0])
P = int(data[1])
Q = int(data[2])
points = []
idx = 3
for i in range(N):
    X = int(data[idx])
    Y = int(data[idx + 1])
    points.append((X, Y))
    idx += 2
points.sort(key=lambda p: p[0])
vals = []
for x, y in points:
    val = Q * y - P * x
    vals.append(val)

def merge_sort(arr):
    if len(arr) <= 1:
        return arr, 0
    mid = len(arr) // 2
    left, inv_left = merge_sort(arr[:mid])
    right, inv_right = merge_sort(arr[mid:])
    merged, inv_merge = merge(left, right)
    return merged, inv_left + inv_right + inv_merge

def merge(left, right):
    merged = []
    i = j = 0
    inv = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
            inv += len(left) - i
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged, inv

_, inversions = merge_sort(vals)
total_pairs = N * (N - 1) // 2
answer = total_pairs - inversions
print(answer)