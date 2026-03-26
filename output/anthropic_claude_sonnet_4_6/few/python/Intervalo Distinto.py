import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    arr = [int(data[i+1]) for i in range(n)]
    
    last_seen = {}
    left = 0
    max_len = 0
    
    for right in range(n):
        val = arr[right]
        if val in last_seen and last_seen[val] >= left:
            left = last_seen[val] + 1
        last_seen[val] = right
        max_len = max(max_len, right - left + 1)
    
    print(max_len)

main()