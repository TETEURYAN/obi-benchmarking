import sys

def main():
    input_data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(input_data[idx]); idx += 1
    
    # Map from left number to (char, right number)
    left_to_piece = {}
    
    for _ in range(n):
        e = int(input_data[idx]); idx += 1
        c = input_data[idx].decode(); idx += 1
        d = int(input_data[idx]); idx += 1
        left_to_piece[e] = (c, d)
    
    result = []
    current = 0
    while current in left_to_piece:
        c, d = left_to_piece[current]
        result.append(c)
        current = d
    
    print(''.join(result))

main()