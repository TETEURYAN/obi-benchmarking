import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    
    # Dicionário para mapear o número esquerdo (E) à letra (C) e ao número direito (D)
    # pieces[E] = (C, D)
    pieces = {}
    
    idx = 1
    for _ in range(n):
        e = int(input_data[idx])
        c = input_data[idx+1]
        d = int(input_data[idx+2])
        pieces[e] = (c, d)
        idx += 3
    
    result = []
    curr = 0
    
    # O quebra-cabeça começa com a peça que tem número esquerdo 0
    # e segue por N peças até o final.
    for _ in range(n):
        c, next_val = pieces[curr]
        result.append(c)
        curr = next_val
        
    sys.stdout.write("".join(result) + "\n")

if __name__ == "__main__":
    solve()