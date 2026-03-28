import sys

def max_subarray_sum(arr):
    max_ending_here = arr[0]
    max_so_far = arr[0]
    for x in arr[1:]:
        max_ending_here = max(x, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far

def max_circular_subarray_sum(arr):
    total_sum = sum(arr)
    max_kadane = max_subarray_sum(arr)
    min_kadane = min_subarray_sum(arr)
    if min_kadane == total_sum:
        return max_kadane
    return max(max_kadane, total_sum - min_kadane)

def min_subarray_sum(arr):
    min_ending_here = arr[0]
    min_so_far = arr[0]
    for x in arr[1:]:
        min_ending_here = min(x, min_ending_here + x)
        min_so_far = min(min_so_far, min_ending_here)
    return min_so_far

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    n = int(data[0])
    arr = list(map(int, data[1:1+n]))
    result = max_circular_subarray_sum(arr)
    print(result)

if __name__ == "__main__":
    main()