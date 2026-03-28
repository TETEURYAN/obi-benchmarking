import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0])
    t = int(data[1])
    
    up = list(map(int, data[2:2+n]))
    down = list(map(int, data[2+n:2+2*n]))
    
    diff = [0] * (n + 2)
    
    idx = 2 + 2 * n
    for _ in range(t):
        i = int(data[idx])
        j = int(data[idx+1])
        idx += 2
        diff[i-1] += 1
        diff[j] -= 1
    
    coverage = [0] * n
    current = 0
    for k in range(n):
        current += diff[k]
        coverage[k] = current
    
    result = []
    for k in range(n):
        if coverage[k] % 2 == 0:
            result.append(str(up[k]))
        else:
            result.append(str(down[k]))
    
    print(' '.join(result))

if __name__ == "__main__":
    main()