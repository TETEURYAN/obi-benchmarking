import sys
from collections import defaultdict

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    k = int(data[1])
    arr = list(map(int, data[2:2+n]))
    
    prefix_count = defaultdict(int)
    prefix_count[0] = 1
    current_sum = 0
    result = 0
    
    for x in arr:
        current_sum += x
        result += prefix_count.get(current_sum - k, 0)
        prefix_count[current_sum] += 1
    
    print(result)

if __name__ == "__main__":
    main()