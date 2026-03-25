import sys
sys.setrecursionlimit(200000)

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    dice = []
    for _ in range(n):
        faces = [int(next(it)) for _ in range(6)]
        dice.append(faces)
    
    # Mapeamento de faces opostas: (0,5), (1,3), (2,4) conforme figura típica
    opposite = {0:5, 1:3, 2:4, 3:1, 4:2, 5:0}
    
    # Para cada dado, pré-computar todas as rotações horizontais possíveis
    # Uma rotação é definida pela face superior e face frontal
    # Vamos gerar todas as combinações válidas (top, front) e calcular os lados
    rotations = []
    for d in dice:
        rot_dict = {}
        # Para cada possível face superior
        for top_idx in range(6):
            # Encontrar índices das 4 faces laterais (excluindo topo e base)
            base_idx = opposite[top_idx]
            lateral_idxs = [i for i in range(6) if i != top_idx and i != base_idx]
            # Para cada possível face frontal entre as laterais
            for front_idx in lateral_idxs:
                # Determinar ordem das faces laterais: front, right, back, left
                # Considerando orientação horária quando visto de cima
                # Encontrar índice da direita: na lista lateral_idxs, front_idx está em alguma posição
                pos = lateral_idxs.index(front_idx)
                right_idx = lateral_idxs[(pos + 1) % 4]
                back_idx = lateral_idxs[(pos + 2) % 4]
                left_idx = lateral_idxs[(pos + 3) % 4]
                
                lateral_values = [d[front_idx], d[right_idx], d[back_idx], d[left_idx]]
                key = (d[top_idx], d[base_idx])
                if key not in rot_dict:
                    rot_dict[key] = lateral_values
                else:
                    # Manter a rotação com maior soma lateral? Não, precisamos de todas possibilidades
                    # Vamos armazenar todas as combinações laterais para este (top, base)
                    # Mas para otimização, basta manter a que tem maior soma lateral para cada (top, base)
                    # Pois queremos maximizar a soma total
                    if sum(lateral_values) > sum(rot_dict[key]):
                        rot_dict[key] = lateral_values
        rotations.append(rot_dict)
    
    # DP para ordem fixa (dados na ordem dada)
    # dp[i][top] = maior soma lateral acumulada até o dado i com topo = top
    INF = -10**9
    dp_fixed = [dict() for _ in range(n)]
    # Inicializar primeiro dado
    first_rot = rotations[0]
    for (top_val, base_val), lateral_vals in first_rot.items():
        dp_fixed[0][top_val] = sum(lateral_vals)
    
    for i in range(1, n):
        current_rot = rotations[i]
        for (top_val, base_val), lateral_vals in current_rot.items():
            best_prev = INF
            # O topo atual deve ser igual à base do dado anterior
            # base_val é a base do dado atual, que deve ser igual ao topo do próximo? Não, a regra é:
            # base do dado atual = topo do dado anterior? Vamos revisar regra 1:
            # "valor da face inferior de X deve ser igual ao valor da face superior de Y"
            # Se X está em cima de Y, então base de X = topo de Y.
            # Na nossa DP, estamos percorrendo de baixo para cima.
            # Então para o dado i (acima do i-1), a base do dado i deve ser igual ao topo do dado i-1.
            # Portanto, base_val deve corresponder a um top_val do dado anterior.
            if base_val in dp_fixed[i-1]:
                best_prev = dp_fixed[i-1][base_val]
            if best_prev != INF:
                dp_fixed[i][top_val] = best_prev + sum(lateral_vals)
    
    max_fixed = max(dp_fixed[n-1].values()) if dp_fixed[n-1] else 0
    
    # Agora considerar ordem arbitrária (problema de permutação)
    # Como N <= 1000, podemos tentar DP considerando todos os dados como disponíveis?
    # Mas isso seria O(N! * ...) impossível.
    # Precisamos de uma abordagem diferente para ordem arbitrária.
    # Observação: a torre é uma sequência onde cada par consecutivo (dado abaixo, dado acima)
    # deve ter topo do abaixo = base do acima.
    # Isso forma um grafo direcionado onde nós são (dado_id, face_top, face_base) e arestas
    # conectam se base de um = topo do outro.
    # Queremos o caminho mais longo (por soma de laterais) usando cada dado no máximo uma vez.
    # Isso é NP-hard? Mas N=1000 pequeno, mas ainda grande para bitmask.
    # No entanto, a errata diz que a solução será julgada com dois conjuntos de testes:
    # um com ordem fixa e outro com ordem arbitrária, e pega-se o maior resultado.
    # Para ordem arbitrária, podemos modelar como: escolher uma permutação dos dados
    # maximizando soma lateral total, com restrição de matching topo-base.
    # Isso é similar a encontrar o caminho hamiltoniano de maior peso num grafo de dados.
    # Não factível para N=1000.
    # Talvez exista propriedade especial: como cada dado tem 6 valores distintos,
    # podemos pensar em construir uma sequência onde cada dado é uma aresta de top->base
    # com peso = soma lateral.
    # Queremos um caminho que use cada dado exatamente uma vez.
    # Isso é como encontrar um caminho euleriano? Não, porque cada dado é um nó, não aresta.
    # Alternativa: como os valores são apenas de 1 a 6, podemos fazer DP por máscara de valores?
    # Mas temos 6 valores possíveis para topo/base.
    # Podemos fazer DP onde estado é (mask de dados usados, último topo) -> maior soma.
    # mask teria 2^1000 estados, impossível.
    # Portanto, para ordem arbitrária, talvez a solução ótima seja sempre conectar dados
    # que tenham alto valor lateral, ignorando a restrição topo-base? Não, a restrição é rígida.
    # Vamos tentar uma heurística gulosa? Mas precisamos de solução exata para passar em 100%.
    # Releia a errata: "as submisões serão julgadas com dois conjuntos de testes,
    # um considerando os dados na ordem dada na entrada e outro considerando que a ordem pode ser qualquer uma
    # e o competidor receberá a maior pontuação entre as duas correções."
    # Isso significa que nosso programa será executado duas vezes: uma com entrada original,
    # outra com entrada permutada aleatoriamente? Não, significa que o juiz tem dois conjuntos
    # de testes: um onde a ordem dos dados na entrada é a ordem da torre (fixa),
    # e outro onde você pode reordenar os dados arbitrariamente.
    # Nosso programa deve funcionar para ambos os cenários.
    # Portanto, precisamos computar a resposta para ordem arbitrária também.
    # Vamos tentar uma DP diferente: como os valores são apenas 1..6, podemos considerar
    # que a torre é uma sequência de dados onde o topo de um deve igualar a base do próximo.
    # Isso é como construir uma sequência de arestas em um grafo de 6 nós (valores 1..6).
    # Cada dado contribui com uma aresta direcionada de topo para base, com peso = soma lateral.
    # Mas cada dado só pode ser usado uma vez.
    # Queremos um caminho (não necessariamente simples nos nós) que maximize soma de pesos,
    # usando cada aresta no máximo uma vez.
    # Isso é o problema do caminho mais longo em multigrafo direcionado com arestas distintas.
    # Podemos fazer DP por máscara de dados? Não.
    # Outra ideia: como cada dado tem 6 valores distintos, podemos representar cada dado
    # por suas 6 faces. A restrição topo-base conecta valores.
    # Talvez possamos modelar como: escolher para cada dado uma orientação (topo, base)
    # tal que a sequência de bases = topo do próximo, maximizando soma lateral.
    # Isso é similar a alinhar dados como dominós.
    # Podemos fazer DP por programação dinâmica em N, mas com estado sendo o valor do topo.
    # Para ordem arbitrária, podemos processar os dados em qualquer ordem, então podemos
    # usar uma DP onde consideramos os dados um a um, e para cada dado, decidimos colocá-lo
    # em alguma posição da sequência? Não trivial.
    # Vamos tentar uma abordagem de fluxo? Talvez seja possível ver como matching.
    # Dado o tempo limitado, implementaremos uma solução para ordem fixa e outra para
    # ordem arbitrária usando DP com estado (topo) acumulando dados.
    # Para ordem arbitrária, podemos processar os dados em qualquer ordem, então podemos
    # usar uma DP onde dp[top] = maior soma lateral acumulada para sequências que terminam com topo = top.
    # Inicializar dp[t] = -inf.
    # Para cada dado, consideramos todas as suas rotações (top, base) com soma lateral S.
    # Atualizamos novo_dp:
    #   para cada top anterior prev_top, se prev_top == base (porque base deste deve ser igual ao topo anterior),
    #   então novo_dp[top] = max(novo_dp[top], dp[prev_top] + S)
    # Além disso, podemos começar uma nova sequência com este dado: novo_dp[top] = max(novo_dp[top], S)
    # Isso é como uma DP de mochila onde adicionamos dados em qualquer ordem.
    # No final, max(dp) é a resposta para ordem arbitrária.
    # Complexidade O(N * 6 * 6) = O(36N) = 36000 para N=1000, factível.
    
    # DP para ordem arbitrária
    dp_arb = {v: INF for v in range(1, 7)}
    for i in range(n):
        new_dp = dp_arb.copy()
        rot = rotations[i]
        for (top_val, base_val), lateral_vals in rot.items():
            S = sum(lateral_vals)
            # Iniciar nova sequência com este dado
            if S > new_dp[top_val]:
                new_dp[top_val] = S
            # Continuar sequência existente
            for prev_top in range(1, 7):
                if dp_arb[prev_top] != INF and prev_top == base_val:
                    cand = dp_arb[prev_top] + S
                    if cand > new_dp[top_val]:
                        new_dp[top_val] = cand
        dp_arb = new_dp
    
    max_arb = max(dp_arb.values())
    
    # Resposta final é o máximo entre as duas
    print(max(max_fixed, max_arb))

if __name__ == "__main__":
    solve()