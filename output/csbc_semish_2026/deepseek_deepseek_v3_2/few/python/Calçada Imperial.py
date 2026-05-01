import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    n = int(data[0])
    seq = list(map(int, data[1:1+n]))
    
    freq = {}
    for num in seq:
        freq[num] = freq.get(num, 0) + 1
    
    unique_nums = list(freq.keys())
    max_len = 0
    
    for i in range(len(unique_nums)):
        a = unique_nums[i]
        max_len = max(max_len, freq[a])
        for j in range(i+1, len(unique_nums)):
            b = unique_nums[j]
            if abs(a - b) > 1:
                continue
            count = 0
            for k in range(n):
                if seq[k] == a or seq[k] == b:
                    count += 1
            max_len = max(max_len, count)
    
    print(max_len)

if __name__ == "__main__":
    main()