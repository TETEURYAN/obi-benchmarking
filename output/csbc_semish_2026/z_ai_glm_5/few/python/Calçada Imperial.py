import sys

def solve():
    # Leitura rápida de toda a entrada
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    # Usamos um iterador para consumir os tokens sequencialmente
    iterator = iter(input_data)
    
    try:
        n_str = next(iterator)
        n = int(n_str)
    except StopIteration:
        return

    # Lista de listas para armazenar os índices de cada valor (1 a N)
    # positions[v] conterá uma lista de índices onde o valor v aparece na sequência
    positions = [[] for _ in range(n + 1)]
    
    for i in range(n):
        try:
            val_str = next(iterator)
            val = int(val_str)
            # O problema garante que 1 <= Vi <= N
            if 1 <= val <= n:
                positions[val].append(i)
        except StopIteration:
            break
            
    # Identificar quais valores realmente aparecem na sequência
    unique_vals = []
    for v in range(1, n + 1):
        if positions[v]:
            unique_vals.append(v)
            
    # Se houver pelo menos um número, podemos sempre marcar 1 número
    # O problema garante N >= 1, então a resposta é pelo menos 1
    max_overall = 1
    
    if not unique_vals:
        print(0)
        return
    
    num_unique = len(unique_vals)
    
    # Iterar sobre todos os pares de valores distintos (u, v)
    for i in range(num_unique):
        u = unique_vals[i]
        pos_u = positions[u]
        len_u_total = len(pos_u)
        
        for j in range(i + 1, num_unique):
            v = unique_vals[j]
            pos_v = positions[v]
            len_v_total = len(pos_v)
            
            # Algoritmo de dois ponteiros para encontrar a maior subsequência alternada
            idx_u = 0
            idx_v = 0
            
            # Tamanhos atuais das subsequências terminando em u ou v
            len_u = 0
            len_v = 0
            
            while idx_u < len_u_total and idx_v < len_v_total:
                if pos_u[idx_u] < pos_v[idx_v]:
                    # u aparece antes de v
                    # Podemos estender uma subsequência terminando em v adicionando este u
                    len_u = len_v + 1
                    idx_u += 1
                else:
                    # v aparece antes de u
                    # Podemos estender uma subsequência terminando em u adicionando este v
                    len_v = len_u + 1
                    idx_v += 1
            
            # Após um dos arrays terminar, ainda podemos adicionar um elemento do array restante
            # se ele aparecer depois do último elemento processado do outro array.
            
            # Se ainda existem u's restantes, podemos adicionar um à sequência terminada em v
            if idx_u < len_u_total:
                len_u = len_v + 1
            
            # Se ainda existem v's restantes, podemos adicionar um à sequência terminada em u
            if idx_v < len_v_total:
                len_v = len_u + 1
            
            current_max = len_u if len_u > len_v else len_v
            if current_max > max_overall:
                max_overall = current_max
                
    print(max_overall)

if __name__ == '__main__':
    solve()