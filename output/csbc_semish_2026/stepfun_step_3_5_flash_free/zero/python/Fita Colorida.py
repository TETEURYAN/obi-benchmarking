
import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    n = int(data[0])
    arr = list(map(int, data[1:1+n]))
    
    INF = 10**9
    d = [INF] * n
    for i in range(n):
        if arr[i] == 0:
            d[i] = 0
    
    for i in range(1, n):
        d[i] = min(d[i], d[i-1] + 1)
    
    for i in range(n-2, -1, -1):
        d[i] = min(d[i], d[i+1] + 1)
    
    res = [str(x if x < 9 else 9) for x in d]
    print(" ".join(res))

if __name__ == "__main__":
    main()
