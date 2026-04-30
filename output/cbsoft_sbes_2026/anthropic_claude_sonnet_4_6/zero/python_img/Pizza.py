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
    # But we need to ensure we don't take all elements (empty remaining)
    # Actually we need at least one element not taken, but we can take 0 elements too
    # The circular subarray wraps around, meaning we exclude a contiguous middle part
    # We need to find min subarray of length 1 to n-1
    
    # Min subarray using kadane on negated
    def kadane_min(a):
        min_sum = 0
        current = 0
        for x in a:
            current += x
            if current < min_sum:
                min_sum = current
            if current > 0:
                current = 0
        return min_sum
    
    # For circular case, we need min subarray that doesn't cover all elements
    # Use prefix sums approach to find min subarray of length 1..n-1
    # Actually let's use a different approach:
    # min subarray of length >= 1 and <= n-1
    
    # We'll compute min subarray sum with length constraint
    # Use the fact that if min_subarray covers all n elements, circular max = total - total = 0
    # But we already handle 0 case (take no slices)
    
    # Simple approach: kadane_min gives min subarray (possibly length n)
    # If min subarray length == n, then circular case gives 0 (same as taking nothing)
    # We handle this by taking max with 0 anyway
    
    min_sub = kadane_min(arr)
    max_circular = total - min_sub
    
    # But if all elements are negative, max_circular = total - total = 0 which is fine
    # since we return max(0, ...)
    
    result = max(max_linear, max_circular, 0)
    return result

def main():
    input_data = sys.stdin.read().split()
    n = int(input_data[0])
    arr = list(map(int, input_data[1:n+1]))
    print(max_subarray_circular(arr))

main()