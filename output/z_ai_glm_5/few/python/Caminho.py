import sys

def solve():
    # Leitura rápida de toda a entrada
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    # O primeiro elemento é N
    n = int(input_data[0])
    
    # Os próximos N elementos são as potências
    # Convertendo para inteiros
    p = list(map(int, input_data[1:n+1]))
    
    max_streak = 0
    current_streak = 0
    
    # Iteramos 2*N vezes para simular a circularidade sem precisar duplicar o array
    # ou criar um array de booleanos auxiliar (economiza memória).
    # Como N <= 500.000, 2*N iterações é perfeitamente aceitável (O(N)).
    for i in range(2 * n):
        # Índice real no array p (módulo N)
        idx = i % n
        next_idx = (idx + 1) % n
        
        # Verifica se é um trecho escuro
        if p[idx] + p[next_idx] < 1000:
            current_streak += 1
            if current_streak > max_streak:
                max_streak = current_streak
            
            # Otimização: se o streak atingir N, cobrimos a pista inteira.
            # Não é possível ter um streak maior que N.
            if max_streak == n:
                break
        else:
            current_streak = 0
            
    print(max_streak)

if __name__ == '__main__':
    solve()