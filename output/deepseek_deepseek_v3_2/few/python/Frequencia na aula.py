import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    
    n = int(data[0])
    numbers = data[1:]
    
    seen = set()
    for num in numbers:
        seen.add(num)
    
    print(len(seen))

if __name__ == "__main__":
    main()