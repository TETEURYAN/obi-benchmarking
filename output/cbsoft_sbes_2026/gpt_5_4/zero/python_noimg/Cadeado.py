import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    
    n = int(data[0])
    ans = 0
    idx = 1
    
    for _ in range(n):
        c = int(data[idx])
        s = int(data[idx + 1])
        idx += 2
        
        d = abs(c - s)
        ans += min(d, 10 - d)
    
    print(ans)

if __name__ == "__main__":
    main()
