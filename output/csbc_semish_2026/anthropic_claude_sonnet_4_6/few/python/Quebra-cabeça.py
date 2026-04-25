import sys

def main():
    data = sys.stdin.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    
    # Build map from left_number -> (letter, right_number)
    left_map = {}
    for _ in range(n):
        e = int(data[idx]); idx += 1
        c = data[idx]; idx += 1
        d = int(data[idx]); idx += 1
        left_map[e] = (c, d)
    
    result = []
    current = 0
    for _ in range(n):
        c, d = left_map[current]
        result.append(c)
        current = d
    
    print(''.join(result))

main()