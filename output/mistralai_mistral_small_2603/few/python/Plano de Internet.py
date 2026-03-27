import sys

def main():
    data = sys.stdin.read().split()
    X = int(data[0])
    N = int(data[1])
    M = list(map(int, data[2:2+N]))
    
    current_quota = X
    for usage in M:
        current_quota = current_quota - usage + X
    
    print(current_quota)

if __name__ == "__main__":
    main()