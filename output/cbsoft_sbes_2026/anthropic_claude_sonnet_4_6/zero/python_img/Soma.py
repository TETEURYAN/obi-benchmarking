from collections import defaultdict
import sys
input = sys.stdin.readline

def main():
    n, k = map(int, input().split())
    xs = list(map(int, input().split()))
    
    # prefix sum approach
    # count subarrays with sum == k
    # prefix[j] - prefix[i] == k => prefix[i] == prefix[j] - k
    
    prefix_count = defaultdict(int)
    prefix_count[0] = 1
    current_sum = 0
    result = 0
    
    for x in xs:
        current_sum += x
        result += prefix_count[current_sum - k]
        prefix_count[current_sum] += 1
    
    print(result)

main()