import sys

def solve():
    # Leitura rápida de toda a entrada
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    # Cria um iterador para converter os tokens para inteiros sob demanda
    iterator = map(int, input_data)
    
    try:
        M = next(iterator)
        N = next(iterator)
    except StopIteration:
        return

    # Array para armazenar o saldo líquido de cada habitante (1 a N)
    balances = [0] * (N + 1)
    total_original = 0
    
    # Processa cada cheque
    # Complexidade O(M)
    for _ in range(M):
        try:
            x = next(iterator)
            v = next(iterator)
            y = next(iterator)
        except StopIteration:
            break
        
        # X emite cheque para Y: X perde V, Y ganha V
        balances[x] -= v
        balances[y] += v
        total_original += v
        
    # Calcula o valor mínimo total compensado
    # É a soma dos saldos positivos (credores líquidos)
    total_min = 0
    for i in range(1, N + 1):
        if balances[i] > 0:
            total_min += balances[i]
            
    # Subtarefa A: É possível diminuir se houver "ciclos" ou redundâncias
    # Isso ocorre se o total original for estritamente maior que o mínimo teórico
    if total_original > total_min:
        print("S")
    else:
        print("N")
        
    # Subtarefa B: Imprime o valor mínimo
    print(total_min)

if __name__ == "__main__":
    solve()