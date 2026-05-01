import sys

def main():
    input_data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(input_data[idx]); idx += 1
    
    # Build a map from left_number -> (letter, right_number)
    pieces = {}
    for _ in range(n):
        e = int(input_data[idx]); idx += 1
        c = input_data[idx].decode(); idx += 1
        d = int(input_data[idx]); idx += 1
        pieces[e] = (c, d)
    
    result = []
    current = 0
    for _ in range(n):
        c, d = pieces[current]
        result.append(c)
        current = d
    
    print(''.join(result))

main()