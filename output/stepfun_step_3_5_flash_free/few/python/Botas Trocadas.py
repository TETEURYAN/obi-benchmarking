import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0])
    left = [0] * 61
    right = [0] * 61
    
    idx = 1
    for _ in range(n):
        size = int(data[idx])
        foot = data[idx + 1]
        idx += 2
        if foot == 'E':
            left[size] += 1
        else:
            right[size] += 1
    
    total_pairs = 0
    for size in range(30, 61):
        total_pairs += min(left[size], right[size])
    
    print(total_pairs)

if __name__ == "__main__":
    main()