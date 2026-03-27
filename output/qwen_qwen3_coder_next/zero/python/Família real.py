
import sys
from collections import defaultdict, deque

def main():
    data = sys.stdin.read().split()
    idx = 0
    N = int(data[idx]); M = int(data[idx+1]); idx += 2
    parents = list(map(int, data[idx:idx+N])); idx += N
    attendees = set(map(int, data[idx:idx+M]))
    
    # Construir a árvore de descendência
    children = defaultdict(list)
    for i in range(N):
        child = i + 1
        parent = parents[i]
        children[parent].append(child)
    
    # Calcular a geração de cada descendente
    generation = {}
    generation[0] = 0  # O rei é a geração 0
    queue = deque([0])
    while queue:
        node = queue.popleft()
        for child in children[node]:
            generation[child] = generation[node] + 1
            queue.append(child)
    
    # Contar o total de descendentes por geração e o número de presentes por geração
    total_by_gen = defaultdict(int)
    present_by_gen = defaultdict(int)
    
    for i in range(1, N+1):
        gen = generation[i]
        total_by_gen[gen] += 1
    
    for person in attendees:
        if person != 0:  # O rei não está na lista de descendentes
            gen = generation[person]
            present_by_gen[gen] += 1
    
    # Calcular as porcentagens
    max_gen = max(generation.values()) if generation else 0
    result = []
    for g in range(1, max_gen + 1):
        total = total_by_gen[g]
        present = present_by_gen[g]
        if total > 0:
            percentage = (present / total) * 100
        else:
            percentage = 0.0
        result.append(f"{percentage:.2f}")
    
    print(" ".join(result)

if __name__ == "__main__":
    main()
