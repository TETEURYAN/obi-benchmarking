import sys

# Aumentar o limite de recursão, embora não seja estritamente necessário para esta solução iterativa.
sys.setrecursionlimit(200000)

def solve():
    # Leitura rápida de toda a entrada
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    iterator = iter(input_data)
    
    try:
        # N: tamanho do conjunto A, M: tamanho da sequência B
        n_str = next(iterator)
        m_str = next(iterator)
        N = int(n_str)
        M = int(m_str)
    except StopIteration:
        return

    # Leitura do conjunto A
    set_A = set()
    for _ in range(N):
        try:
            set_A.add(int(next(iterator)))
        except StopIteration:
            break
            
    # Leitura da sequência B
    sequence_B = []
    for _ in range(M):
        try:
            sequence_B.append(int(next(iterator)))
        except StopIteration:
            break

    # Conjunto para armazenar os números válidos que já estão em B
    # Usamos um set para busca O(1)
    current_B_set = set()
    # Lista para manter a ordem e permitir iteração rápida (otimização leve sobre iteração de set)
    current_B_list = []

    for num in sequence_B:
        # Verifica a primeira condição: num pertence a A
        if num in set_A:
            current_B_set.add(num)
            current_B_list.append(num)
            continue
        
        # Verifica a segunda condição: num é soma de dois números em B
        # Complexidade: O(|B|) por iteração. Total O(M^2).
        # Com M=10^4, M^2 = 10^8, que é o limite aceitável para Python em competições (aprox 1-2s).
        found = False
        for y in current_B_list:
            # Se num = y + z, então z = num - y
            # Verificamos se z está no conjunto de números válidos atual
            if (num - y) in current_B_set:
                found = True
                break
        
        if found:
            current_B_set.add(num)
            current_B_list.append(num)
        else:
            # Encontrou a primeira jogada inválida
            print(num)
            return

    # Se todas as jogadas são válidas
    print("sim")

if __name__ == "__main__":
    solve()