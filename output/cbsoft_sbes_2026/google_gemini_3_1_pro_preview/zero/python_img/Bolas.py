import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    counts = {}
    for num in data:
        counts[num] = counts.get(num, 0) + 1
    
    if max(counts.values()) > 4:
        print("N")
    else:
        print("S")

if __name__ == '__main__':
    main()