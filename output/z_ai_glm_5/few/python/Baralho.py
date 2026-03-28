import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    s = input_data[0]
    
    # Mapeamento dos naipes para índices: C=0, E=1, U=2, P=3
    suit_map = {'C': 0, 'E': 1, 'U': 2, 'P': 3}
    
    # Conjuntos para armazenar as cartas vistas de cada naipe
    seen = [set() for _ in range(4)]
    # Flags para verificar duplicatas
    duplicate = [False] * 4
    
    # Processar a string em passos de 3 caracteres
    n = len(s)
    for i in range(0, n, 3):
        card = s[i:i+3]
        val_str = card[:2]
        suit_char = card[2]
        
        val = int(val_str)
        idx = suit_map[suit_char]
        
        if val in seen[idx]:
            duplicate[idx] = True
        else:
            seen[idx].add(val)
            
    # Gerar saída para os 4 naipes na ordem C, E, U, P
    output_lines = []
    for i in range(4):
        if duplicate[i]:
            output_lines.append("erro")
        else:
            missing = 13 - len(seen[i])
            output_lines.append(str(missing))
            
    print('\n'.join(output_lines))

if __name__ == '__main__':
    solve()