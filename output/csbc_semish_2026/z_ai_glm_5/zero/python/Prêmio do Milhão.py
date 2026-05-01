import sys

def main():
    data = sys.stdin.read().split()
    
    if not data:
        return

    iterator = iter(data)
    n = int(next(iterator))
    
    target = 1000000
    total = 0
    days = 0
    
    for _ in range(n):
        accesses = int(next(iterator))
        total += accesses
        days += 1
        if total >= target:
            break
            
    print(days)

if __name__ == "__main__":
    main()
```