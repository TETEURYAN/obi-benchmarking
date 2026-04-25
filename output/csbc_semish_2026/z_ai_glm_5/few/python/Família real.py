import sys
from collections import deque

# Aumentar o limite de recursão, conforme diretrizes, embora a solução use BFS
sys.setrecursionlimit(200000)

def main():
    # Leitura rápida de toda a entrada
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    iterator = iter(input_data)
    
    try:
        N = int(next(iterator))
        M = int(next(iterator))
    except StopIteration:
        return

    # Leitura dos pais
    parents = []
    for _ in range(N):
        parents.append(int(next(iterator)))
        
    # Leitura dos participantes
    attendees = set()
    for _ in range(M):
        attendees.add(int(next(iterator)))
    
    # Construção da árvore de filhos (adjacência)
    # Os nós são identificados de 0 a N. 0 é o Rei.
    children = [[] for _ in range(N + 1)]
    
    # O input fornece o pai do descendente i (1-based) na posição i-1
    for i in range(N):
        descendant_id = i + 1
        parent_id = parents[i]
        children[parent_id].append(descendant_id)
        
    # BFS para calcular gerações
    # gen_counts[g] guarda o número de descendentes na geração g
    # att_counts[g] guarda o número de participantes na geração g
    # Índice 0 não usado (Rei), geração 1 são filhos do Rei.
    
    # Como N <= 10000, a profundidade máxima é menor que N, mas alocamos N+2 para segurança
    gen_counts = [0] * (N + 2)
    att_counts = [0] * (N + 2)
    
    queue = deque([(0, 0)]) # (nó, geração)
    max_gen = 0
    
    while queue:
        node, gen = queue.popleft()
        
        for child in children[node]:
            child_gen = gen + 1
            gen_counts[child_gen] += 1
            
            if child in attendees:
                att_counts[child_gen] += 1
            
            if child_gen > max_gen:
                max_gen = child_gen
                
            queue.append((child, child_gen))
            
    # Gerar a saída
    results = []
    for g in range(1, max_gen + 1):
        total = gen_counts[g]
        attended = att_counts[g]
        
        if total > 0:
            percentage = (attended / total) * 100.0
        else:
            percentage = 0.0
            
        results.append(f"{percentage:.2f}")
        
    print(*(results))

if __name__ == "__main__":
    main()