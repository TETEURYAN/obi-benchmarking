import sys

def main():
    # Leitura rápida de toda a entrada
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    # Converte todos os tokens para inteiros de uma vez
    nums = list(map(int, input_data))
    
    idx = 0
    
    # Leitura de E, M, D
    E = nums[idx]
    M = nums[idx+1]
    D = nums[idx+2]
    idx += 3
    
    # Armazena os pares que querem ficar juntos (M pares)
    # Como a ordem não importa para a verificação, guardamos como tuplas
    pairs_M = []
    for _ in range(M):
        u = nums[idx]
        v = nums[idx+1]
        pairs_M.append((u, v))
        idx += 2
        
    # Armazena os pares que não querem ficar juntos (D pares)
    pairs_D = []
    for _ in range(D):
        u = nums[idx]
        v = nums[idx+1]
        pairs_D.append((u, v))
        idx += 2
        
    # Processa os grupos para determinar o grupo de cada estudante
    # group_id[i] retorna o identificador do grupo do estudante i
    # Tamanho E + 1 pois os estudantes são numerados de 1 a E
    group_id = [0] * (E + 1)
    
    num_groups = E // 3
    
    for g in range(num_groups):
        s1 = nums[idx]
        s2 = nums[idx+1]
        s3 = nums[idx+2]
        idx += 3
        
        group_id[s1] = g
        group_id[s2] = g
        group_id[s3] = g
        
    violations = 0
    
    # Verifica restrições do tipo M (querem ficar juntos)
    # A restrição é violada se estão em grupos diferentes
    for u, v in pairs_M:
        if group_id[u] != group_id[v]:
            violations += 1
            
    # Verifica restrições do tipo D (não querem ficar juntos)
    # A restrição é violada se estão no mesmo grupo
    for u, v in pairs_D:
        if group_id[u] == group_id[v]:
            violations += 1
            
    print(violations)

if __name__ == "__main__":
    main()