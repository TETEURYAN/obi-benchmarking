import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    it = iter(data)
    S = int(next(it))
    T = int(next(it))
    
    edges = set()
    for _ in range(T):
        x = int(next(it))
        y = int(next(it))
        if x > y:
            x, y = y, x
        edges.add((x, y))
    
    P = int(next(it))
    possible = 0
    
    for _ in range(P):
        N = int(next(it))
        seq = [int(next(it)) for _ in range(N)]
        ok = True
        for i in range(N-1):
            a = seq[i]
            b = seq[i+1]
            if a > b:
                a, b = b, a
            if (a, b) not in edges:
                ok = False
                break
        if ok:
            possible += 1
    
    print(possible)

if __name__ == "__main__":
    main()