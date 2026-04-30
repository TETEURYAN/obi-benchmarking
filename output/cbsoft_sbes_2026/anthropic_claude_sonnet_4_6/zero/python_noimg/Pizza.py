import sys

def max_subarray_circular(arr):
    n = len(arr)
    if n == 0:
        return 0
    
    # Kadane's algorithm for maximum subarray (linear)
    def kadane(a):
        max_sum = 0
        current = 0
        for x in a:
            current += x
            if current > max_sum:
                max_sum = current
            if current < 0:
                current = 0
        return max_sum
    
    # Case 1: max subarray is not circular
    max_linear = kadane(arr)
    
    # Case 2: max subarray is circular
    # Total sum - min subarray sum (but min subarray must not be the entire array)
    total = sum(arr)
    
    # Find minimum subarray sum using kadane on negated array
    # But we need to ensure we don't take empty subarray for min (i.e., min subarray is at least 1 element)
    # Actually for circular case, we need at least 1 element remaining outside
    # So min subarray can be at most n-1 elements
    
    # Minimum subarray sum (non-empty)
    min_sum = 0
    current_min = 0
    min_val = arr[0]
    current_min = arr[0]
    min_sum = arr[0]
    for i in range(1, n):
        current_min = min(arr[i], current_min + arr[i])
        min_sum = min(min_sum, current_min)
    
    # If all elements are negative, min_sum = total, circular would be total - total = 0
    # which means we take no elements (allowed since answer >= 0)
    if total - min_sum > 0 and min_sum != total:
        max_circular = total - min_sum
    else:
        max_circular = 0
    
    return max(max_linear, max_circular, 0)

def main():
    input_data = sys.stdin.read().split()
    n = int(input_data[0])
    arr = list(map(int, input_data[1:n+1]))
    
    print(max_subarray_circular(arr))

main()