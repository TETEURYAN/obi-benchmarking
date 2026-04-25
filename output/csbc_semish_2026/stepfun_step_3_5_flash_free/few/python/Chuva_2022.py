import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    s = int(data[1])
    arr = list(map(int, data[2:2+n]))
    
    prefix_sum = 0
    freq = {0: 1}
    count = 0
    
    for x in arr:
        prefix_sum += x
        target = prefix_sum - s
        if target in freq:
            count += freq[target]
        freq[prefix_sum] = freq.get(prefix_sum, 0) + 1
    
    print(count)

if __name__ == "__main__":
    main()