import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    n = int(data[0])
    ops = list(map(int, data[1:1+n]))
    
    a = 0
    b = 0
    
    for op in ops:
        if op == 1:
            a ^= 1
        elif op == 2:
            a ^= 1
            b ^= 1
    
    print(a)
    print(b)

if __name__ == "__main__":
    main()