import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    seq = list(map(int, data[1:1+n]))
    
    last_seen = {}
    max_len = 0
    left = 0
    
    for right, val in enumerate(seq):
        if val in last_seen and last_seen[val] >= left:
            left = last_seen[val] + 1
        last_seen[val] = right
        max_len = max(max_len, right - left + 1)
    
    print(max_len)

if __name__ == "__main__":
    main()