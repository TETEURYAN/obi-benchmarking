import sys
import bisect

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    c = int(data[0])
    t = int(data[1])
    
    raios = list(map(int, data[2:2+c]))
    raios_quad = [r*r for r in raios]
    
    total = 0
    idx = 2 + c
    for _ in range(t):
        x = int(data[idx])
        y = int(data[idx+1])
        idx += 2
        d2 = x*x + y*y
        pos = bisect.bisect_left(raios_quad, d2)
        total += c - pos
    
    print(total)

if __name__ == "__main__":
    main()