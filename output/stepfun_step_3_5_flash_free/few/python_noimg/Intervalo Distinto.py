import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    arr = list(map(int, data[1:1+n]))
    
    max_val = 100000
    count = [0] * (max_val + 1)
    left = 0
    max_len = 0
    
    for right in range(n):
        num = arr[right]
        count[num] += 1
        while count[num] > 1:
            count[arr[left]] -= 1
            left += 1
        current_len = right - left + 1
        if current_len > max_len:
            max_len = current_len
    
    print(max_len)

if __name__ == "__main__":
    main()