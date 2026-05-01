
import sys

def main():
    n = int(sys.stdin.readline())
    heights = list(map(int, sys.stdin.readline().split()))
    
    max_height = max(heights)
    count = [0] * (max_height + 2)
    
    for h in heights:
        count[h] += 1
    
    max_pieces = 0
    current = 0
    for h in range(max_height, 0, -1):
        current += count[h]
        if current > max_pieces:
            max_pieces = current
    
    print(max_pieces)

if __name__ == "__main__":
    main()
