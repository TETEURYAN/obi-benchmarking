import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    A = [int(next(it)) for _ in range(n)]
    B = [int(next(it)) for _ in range(m)]
    
    setA = set(A)
    S = set()
    
    for b in B:
        if b in setA:
            S.add(b)
            continue
        found = False
        for y in S:
            if (b - y) in S:
                found = True
                break
        if not found:
            print(b)
            return
        S.add(b)
    print("sim")

if __name__ == "__main__":
    main()