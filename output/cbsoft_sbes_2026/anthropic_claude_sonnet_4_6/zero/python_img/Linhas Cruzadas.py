import sys

def merge_sort_count(arr):
    if len(arr) <= 1:
        return arr, 0
    mid = len(arr) // 2
    left, left_inv = merge_sort_count(arr[:mid])
    right, right_inv = merge_sort_count(arr[mid:])
    merged = []
    inversions = left_inv + right_inv
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            inversions += len(left) - i
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged, inversions

def main():
    input_data = sys.stdin.read().split()
    n = int(input_data[0])
    arr = list(map(int, input_data[1:n+1]))
    _, count = merge_sort_count(arr)
    print(count)

sys.setrecursionlimit(300000)
main()