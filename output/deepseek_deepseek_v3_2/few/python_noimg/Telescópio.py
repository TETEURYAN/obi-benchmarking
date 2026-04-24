import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    
    idx = 0
    A = int(data[idx]); idx += 1
    N = int(data[idx]); idx += 1
    
    count = 0
    for _ in range(N):
        F = int(data[idx]); idx += 1
        if F * A >= 40_000_000:
            count += 1
    
    print(count)

if __name__ == "__main__":
    main()