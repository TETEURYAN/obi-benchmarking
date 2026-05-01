
import sys

def main():
    input = sys.stdin.read
    data = input().split()
    N = int(data[0])
    M = int(data[1])
    
    if 3 * M < N:
        print(0)
        return
    
    min_each = max(1, N - 2 * M)
    max_each = min(M, N - 2)
    
    total = 0
    for x in range(min_each, max_each + 1):
        rem = N - x
        min_y = max(1, rem - M)
        max_y = min(M, rem - 1)
        if min_y <= max_y:
            total += max_y - min_y + 1
    
    print(total)

if __name__ == "__main__":
    main()
