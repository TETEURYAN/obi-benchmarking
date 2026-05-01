import sys
from collections import defaultdict

def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    k = int(data[1])
    x = list(map(int, data[2:2+n]))
    
    # prefix sums
    # count subarrays with sum == k
    # prefix[j] - prefix[i] == k => prefix[i] == prefix[j] - k
    
    count = 0
    freq = defaultdict(int)
    freq[0] = 1
    prefix = 0
    
    for i in range(n):
        prefix += x[i]
        count += freq[prefix - k]
        freq[prefix] += 1
    
    print(count)

main()