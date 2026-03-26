
import sys

# Aumentar o limite de recursão é uma boa prática, embora a solução seja iterativa.
sys.setrecursionlimit(30000)

def solve():
    # Lê toda a entrada padrão de uma vez para eficiência
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    iterator = iter(input_data)
    
    try:
        N = int(next(iterator))
        M = int(next(iterator))
    except StopIteration:
        return

    # parents[i] armazena o pai/mãe do descendente i.
    # O índice 0 não é usado para descendentes, mas o rei é 0.
    parents = [0] * (N + 1)
    
    # Lendo os pais dos descendentes 1 a N
    for i in range(1, N + 1):
        parents[i] = int(next(iterator))
        
    # Lendo a lista de participantes
    attendees = []
    for _ in range(M):
        attendees.append(int(next(iterator)))
        
    # Array para memoização da geração de cada descendente
    # -1 indica que ainda não foi calculado.
    # gen[0] = 0 (O rei está na geração 0)
    gen = [-1] * (N + 1)
    gen[0] = 0
    
    # Função iterativa para calcular a geração de um descendente
    def calculate_generation(u):
        if gen[u] != -1:
            return gen[u]
        
        path = []
        curr = u
        # Sube na árvore genealógica até encontrar um ancestral com geração conhecida
        while gen[curr] == -1:
            path.append(curr)
            curr = parents[curr]
            
        # curr agora tem uma geração conhecida (gen[curr])
        current_gen = gen[curr]
        
        # Atribui a geração para todos os nós no caminho percorrido
        for node in reversed(path):
            current_gen += 1
            gen[node] = current_gen
            
        return gen[u]

    # Arrays para contagem
    # O tamanho N+2 é seguro pois a profundidade máxima da árvore é N
    total_in_gen = [0] * (N + 2)
    attended_in_gen = [0] * (N + 2)
    
    max_gen_found = 0
    
    # Calcula geração para todos os descendentes e conta o total por geração
    for i in range(1, N + 1):
        g = calculate_generation(i)
        total_in_gen[g] += 1
        if g > max_gen_found:
            max_gen_found = g
            
    # Calcula geração para os participantes e conta comparecimentos por geração
    for u in attendees:
        g = calculate_generation(u)
        attended_in_gen[g] += 1
        
    # Prepara a saída
    output = []
    for g in range(1, max_gen_found + 1):
        total = total_in_gen[g]
        attended = attended_in_gen[g]
        
        if total == 0:
            percentage = 0.0
        else:
            percentage = (attended / total) * 100.0
            
        output.append(f"{percentage:.2f}")
        
    print(" ".join(output))

if __name__ == '__main__':
    solve()
