from collections import defaultdict
import sys
input = sys.stdin.readline

def main():
    n, k = map(int, input().split())
    x = list(map(int, input().split()))
    
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i+1] = prefix[i] + x[i]
    
    count = defaultdict(int)
    result = 0
    
    for i in range(n + 1):
        target = prefix[i] - k
        if target in count:
            result += count[target]
        count[prefix[i]] += 1
    
    print(result)

main()