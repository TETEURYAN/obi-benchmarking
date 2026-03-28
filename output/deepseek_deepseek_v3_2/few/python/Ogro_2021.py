import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    N = int(data[0])
    
    if N <= 5:
        left = 'I' * N if N > 0 else '*'
        right = '*'
    else:
        left = 'IIIII'
        right = 'I' * (N - 5)
    
    print(left)
    print(right)

if __name__ == "__main__":
    main()