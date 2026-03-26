
import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    n = int(data[0])
    pieces = []
    idx = 1
    for _ in range(n):
        e = int(data[idx]); idx += 1
        c = data[idx]; idx += 1
        d = int(data[idx]); idx += 1
        pieces.append((e, c, d))
    
    # Mapeia número esquerdo para (letra, número direito)
    left_map = {}
    # Conjunto de números direitos para encontrar o início
    right_set = set()
    
    for e, c, d in pieces:
        left_map[e] = (c, d)
        right_set.add(d)
    
    # Encontrar a peça inicial: número esquerdo que não aparece em right_set
    start = None
    for e, c, d in pieces:
        if e not in right_set:
            start = e
            break
    
    result = []
    current = start
    while True:
        c, d = left_map[current]
        result.append(c)
        if d == 1:  # última peça
            break
        current = d
    
    print(''.join(result))

if __name__ == "__main__":
    main()
