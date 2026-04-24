import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    n = int(data[0])
    L = list(map(int, data[1:1+n]))
    
    total = sum(L)
    if total % 2 != 0:
        print("N")
        return
    
    half = total // 2
    prefix = 0
    seen = set()
    possible = False
    
    for length in L:
        prefix += length
        if prefix > half:
            break
        seen.add(prefix)
    
    if half in seen:
        prefix = 0
        for length in L:
            prefix += length
            if prefix > half:
                break
            if (prefix + half) % total in seen:
                possible = True
                break
    
    print("S" if possible else "N")

if __name__ == "__main__":
    main()