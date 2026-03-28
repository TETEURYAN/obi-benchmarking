import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    heights = list(map(int, data[1:1+n]))
    
    pieces = 0
    prev = 0
    for h in heights:
        if h > prev:
            pieces += 1
        prev = h
    
    print(pieces)

if __name__ == "__main__":
    main()