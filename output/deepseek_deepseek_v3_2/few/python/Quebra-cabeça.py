import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    idx = 0
    n = int(data[idx])
    idx += 1
    
    left_to_piece = {}
    right_to_piece = {}
    
    for _ in range(n):
        e = int(data[idx])
        c = data[idx + 1]
        d = int(data[idx + 2])
        idx += 3
        
        left_to_piece[e] = (c, d)
        right_to_piece[d] = (c, e)
    
    # Encontrar a primeira peça (esquerda = 0)
    current_left = 0
    result_chars = []
    
    while True:
        c, d = left_to_piece[current_left]
        result_chars.append(c)
        if d == 1:
            break
        current_left = d
    
    print(''.join(result_chars))

if __name__ == "__main__":
    main()