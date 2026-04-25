import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    
    n = int(data[0])
    boots = data[1:]
    
    left = {}
    right = {}
    
    idx = 0
    while idx < len(boots):
        m = int(boots[idx])
        l = boots[idx + 1]
        idx += 2
        if l == 'E':
            left[m] = left.get(m, 0) + 1
        else:
            right[m] = right.get(m, 0) + 1
    
    pairs = 0
    for size in left:
        if size in right:
            pairs += min(left[size], right[size])
    
    print(pairs)

if __name__ == "__main__":
    main()