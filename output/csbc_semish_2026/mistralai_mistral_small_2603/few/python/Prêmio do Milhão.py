import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    accesses = list(map(int, data[1:n+1]))
    
    total = 0
    days = 0
    for a in accesses:
        days += 1
        total += a
        if total >= 1000000:
            break
    
    print(days)

if __name__ == "__main__":
    main()