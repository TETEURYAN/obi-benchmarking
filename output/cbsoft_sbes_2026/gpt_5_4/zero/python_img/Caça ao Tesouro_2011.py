import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    
    it = iter(data)
    N = int(next(it))
    K = int(next(it))
    
    clues = []
    for _ in range(K):
        x = int(next(it))
        y = int(next(it))
        d = int(next(it))
        clues.append((x, y, d))
    
    ans = None
    count = 0
    
    for tx in range(N):
        for ty in range(N):
            ok = True
            for x, y, d in clues:
                if abs(tx - x) + abs(ty - y) != d:
                    ok = False
                    break
            if ok:
                count += 1
                if count == 1:
                    ans = (tx, ty)
                else:
                    print("-1 -1")
                    return
    
    print(ans[0], ans[1])

if __name__ == "__main__":
    main()
