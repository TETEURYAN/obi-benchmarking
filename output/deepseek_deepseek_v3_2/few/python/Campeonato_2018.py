import sys

def solve():
    data = list(map(int, sys.stdin.read().split()))
    pos = [0] * 17
    for i, val in enumerate(data):
        pos[val] = i + 1
    
    kung_pos = pos[1]
    lu_pos = pos[9]
    
    # Ajusta para índice 0-15
    k = kung_pos - 1
    l = lu_pos - 1
    
    # Simula torneio eliminatório
    round_names = ["oitavas", "quartas", "semifinal", "final"]
    for r in range(4):
        # Verifica se estão no mesmo grupo de 2^(r+1) posições
        group_size = 1 << (r + 1)
        if k // group_size == l // group_size:
            print(round_names[r])
            return

if __name__ == "__main__":
    solve()