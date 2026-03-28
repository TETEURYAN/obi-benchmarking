import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    P = list(map(int, data[1:1+n]))
    
    A = [0] * n
    for i in range(n):
        if P[i] + P[(i+1) % n] < 1000:
            A[i] = 1
    
    if all(A):
        print(n)
        return
    
    max_run = 0
    cur = 0
    for x in A:
        if x:
            cur += 1
            if cur > max_run:
                max_run = cur
        else:
            cur = 0
    
    prefix = 0
    for x in A:
        if x:
            prefix += 1
        else:
            break
    
    suffix = 0
    for x in reversed(A):
        if x:
            suffix += 1
        else:
            break
    
    ans = max(max_run, prefix + suffix)
    print(ans)

if __name__ == "__main__":
    main()