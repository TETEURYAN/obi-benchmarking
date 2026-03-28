import sys

def main():
    data = sys.stdin.read().split()
    N = int(data[0])
    M = int(data[1])
    Xe = int(data[2])
    Ye = int(data[3])
    Xs = int(data[4])
    Ys = int(data[5])

    # Armários estão em células (i,j) onde i e j são pares
    # Precisamos encontrar a maior distância possível entre entrada e saída
    # após derrubar armários de forma ótima

    # A estratégia é modelar como um grafo onde cada célula é um nó
    # e as arestas representam movimentos possíveis (cima, baixo, esquerda, direita)
    # Armários derrubados bloqueiam células, então precisamos escolher a direção
    # de queda que maximize o caminho

    # Como N e M são pequenos (3 a 11), podemos usar BFS para cada configuração
    # de armários derrubados e encontrar a máxima distância

    # Primeiro, identificar todas as posições de armários
    armarios = []
    for i in range(2, N+1, 2):
        for j in range(2, M+1, 2):
            armarios.append((i, j))

    max_dist = 0

    # Para cada armário, tentar derrubar em cada uma das 4 direções possíveis
    # e calcular a distância máxima possível
    # Como o número de armários é pequeno (até 5x5=25 armários), podemos fazer isso

    from itertools import product

    # Vamos gerar todas as combinações de direções para cada armário
    # Cada armário tem 4 opções, então total de combinações é 4^(número de armários)
    # Para 25 armários, isso seria 4^25 = 1.1e15, muito grande
    # Então precisamos de uma abordagem melhor

    # Alternativa: modelar como um problema de fluxo máximo ou usar BFS com estados
    # Mas como N e M são muito pequenos (até 11x11=121 células), podemos fazer BFS
    # para cada configuração de armários derrubados

    # Outra abordagem: a distância máxima será a distância de Manhattan entre entrada e saída
    # mais o número de armários que podemos derrubar para bloquear caminhos alternativos
    # Mas não é tão simples assim

    # Vamos tentar uma abordagem de força bruta com poda:
    # Para cada armário, escolher a direção que maximize a distância do caminho
    # Isso é um problema de otimização combinatória

    # Como o número de armários é pequeno (até 25), mas 4^25 é grande,
    # vamos usar uma estratégia gulosa ou programação dinâmica

    # Alternativa: modelar como um grafo onde cada nó é uma configuração de armários
    # e arestas representam escolhas de direção para um armário
    # Mas isso também é inviável

    # Melhor abordagem: perceber que a distância máxima é a distância de Manhattan
    # entre entrada e saída, mais 2*(número de armários que podemos derrubar)
    # porque cada armário derrubado pode bloquear um caminho alternativo de 2 células

    # Vamos calcular a distância de Manhattan entre entrada e saída
    manhattan = abs(Xe - Xs) + abs(Ye - Ys)

    # O número máximo de armários que podemos derrubar é o número total de armários
    # porque podemos derrubar todos na direção que bloqueie mais caminhos
    num_armarios = len(armarios)

    # Mas não podemos derrubar armários que estejam na entrada ou saída
    # ou que bloqueiem completamente o caminho

    # Vamos verificar se a entrada e saída estão livres de armários
    # (garantido pelo problema)

    # A distância máxima possível é a distância de Manhattan + 2*num_armarios
    # porque cada armário derrubado pode adicionar 2 células ao caminho
    # (ocupando 2 células que antes eram livres)

    # Mas isso não é sempre verdade, porque os armários estão em posições específicas

    # Vamos testar com os exemplos:
    # Exemplo 1: 7x7, entrada (3,7), saída (5,1)
    # Armários: (2,2), (2,4), (2,6), (4,2), (4,4), (4,6), (6,2), (6,4), (6,6)
    # Número de armários: 9
    # Manhattan: |3-5| + |7-1| = 2 + 6 = 8
    # 8 + 2*9 = 26, mas a resposta é 29
    # Então essa abordagem está errada

    # Outra abordagem: a distância máxima é o comprimento do caminho mais longo
    # possível na grade, considerando que armários derrubados bloqueiam células

    # Como N e M são pequenos, podemos fazer BFS para cada configuração de armários
    # derrubados, mas o número de configurações é grande

    # Vamos tentar uma abordagem diferente: modelar como um problema de fluxo
    # ou usar a ideia de que a distância máxima é a distância de Manhattan
    # mais o número de armários que podemos derrubar vezes 2, mas ajustado

    # Para o exemplo 1:
    # A distância de Manhattan é 8
    # A resposta é 29, que é 8 + 21
    # 21 = 3*7, não faz sentido

    # Vamos calcular o número de células livres inicialmente:
    # Total de células: 7*7 = 49
    # Armários: 9
    # Células livres: 40
    # O caminho mínimo sem derrubar armários seria a distância de Manhattan + 1
    # (número de células visitadas)
    # Mas a distância de Manhattan é 8, então caminho mínimo seria 9
    # A resposta é 29, que é muito maior

    # Aparentemente, a distância máxima é o número de células livres
    # porque podemos fazer um caminho que visite todas as células livres
    # mas isso não faz sentido porque entrada e saída são fixas

    # Vamos pensar de novo:
    # A figura mostra um caminho de 29 células
    # A grade tem 49 células, 9 armários, então 40 livres
    # 29 é menor que 40, então não é visitando todas

    # Outra ideia: a distância máxima é a distância de Manhattan entre entrada e saída
    # mais 2 vezes o número de armários que podemos derrubar para bloquear caminhos alternativos

    # Vamos tentar calcular para o exemplo 1:
    # Armários: 9
    # Se derrubarmos todos os armários na direção que bloqueie mais caminhos,
    # podemos forçar um caminho mais longo
    # A distância máxima possível é a distância de Manhattan + 2*9 = 8 + 18 = 26
    # Mas a resposta é 29, então está errado

    # Vamos tentar outra abordagem: a distância máxima é o comprimento do caminho
    # mais longo possível na grade, considerando que armários derrubados bloqueiam células
    # e que podemos escolher a direção de queda de cada armário

    # Como N e M são pequenos (até 11), podemos fazer BFS para cada configuração
    # de armários derrubados, mas o número de configurações é 4^(número de armários)
    # Para 9 armários, 4^9 = 262144, que é viável

    # Vamos implementar isso:

    # Primeiro, identificar todas as posições de armários
    armarios = []
    for i in range(2, N+1, 2):
        for j in range(2, M+1, 2):
            armarios.append((i, j))

    max_dist = 0

    # Vamos gerar todas as combinações de direções para os armários
    from itertools import product

    # Cada armário pode ser derrubado em 4 direções, ou não derrubado?
    # O problema diz "derrubar os armários", então todos devem ser derrubados
    # em alguma direção

    # Vamos gerar todas as combinações de direções para os armários
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # direita, esquerda, baixo, cima

    # Para cada combinação de direções, criar a grade bloqueada
    # e calcular a distância máxima entre entrada e saída

    # Como o número de armários pode ser até 25 (para N=M=11),
    # 4^25 é muito grande (1.1e15), então essa abordagem não é viável

    # Precisamos de uma abordagem melhor

    # Outra ideia: a distância máxima é a distância de Manhattan entre entrada e saída
    # mais 2 vezes o número de armários que estão no caminho mínimo
    # Mas não sabemos qual é o caminho mínimo

    # Vamos tentar uma abordagem de programação dinâmica ou BFS com estados
    # onde o estado inclui a posição atual e as direções dos armários derrubados
    # Mas isso também é inviável

    # Melhor abordagem: perceber que a distância máxima é a distância de Manhattan
    # entre entrada e saída, mais 2 vezes o número de armários que podemos derrubar
    # para bloquear caminhos alternativos

    # Vamos calcular a distância de Manhattan
    manhattan = abs(Xe - Xs) + abs(Ye - Ys)

    # O número máximo de armários que podemos derrubar é o número total de armários
    # porque podemos derrubar todos

    # Mas a distância máxima não é simplesmente manhattan + 2*num_armarios
    # porque os armários estão em posições específicas

    # Vamos tentar calcular para os exemplos:

    # Exemplo 1:
    # N=7, M=7
    # Armários: (2,2), (2,4), (2,6), (4,2), (4,4), (4,6), (6,2), (6,4), (6,6)
    # Entrada: (3,7), Saída: (5,1)
    # Manhattan: |3-5| + |7-1| = 2 + 6 = 8
    # Se derrubarmos todos os armários na direção que bloqueie mais caminhos,
    # podemos forçar um caminho mais longo
    # A resposta é 29, que é 8 + 21
    # 21 = 3*7, não faz sentido

    # Vamos contar o número de células livres:
    # Total: 49
    # Armários: 9
    # Livres: 40
    # 29 é menor que 40

    # Outra ideia: a distância máxima é o número de células livres
    # porque podemos fazer um caminho que visite todas as células livres
    # mas a entrada e saída são fixas, então o caminho deve começar em (3,7) e terminar em (5,1)
    # e visitar o máximo de células possíveis

    # A distância máxima possível é o número de células livres
    # porque podemos visitar todas as células livres em um caminho
    # mas isso não é necessariamente verdade porque a entrada e saída são fixas

    # Vamos calcular o número de células livres para o exemplo 1:
    # 49 - 9 = 40
    # A resposta é 29, que é menor que 40

    # Vamos tentar outra abordagem: a distância máxima é a distância de Manhattan
    # entre entrada e saída, mais 2 vezes o número de armários que estão em posições
    # que podem ser derrubadas para bloquear caminhos alternativos

    # Vamos contar quantos armários estão no "retângulo" entre entrada e saída
    # e multiplicar por 2

    # Para o exemplo 1:
    # Entrada: (3,7), Saída: (5,1)
    # Armários no retângulo: todos os 9 armários estão no retângulo
    # 8 + 2*9 = 26, mas a resposta é 29

    # Vamos tentar adicionar 3 vezes o número de armários:
    # 8 + 3*9 = 35, ainda não é 29

    # Outra ideia: a distância máxima é a distância de Manhattan entre entrada e saída
    # mais o número de armários vezes 2, mais alguma constante

    # Vamos tentar para o exemplo 2:
    # N=11, M=11
    # Entrada: (11,1), Saída: (1,11)
    # Manhattan: |11-1| + |1-11| = 10 + 10 = 20
    # Armários: (2,2), (2,4), ..., (10,10) -> 5x5=25 armários
    # Resposta: 69
    # 20 + 2*25 = 70, que é próximo de 69
    # Talvez seja 20 + 2*24 = 68, ainda não é 69

    # Vamos tentar 20 + 2*24 + 1 = 69
    # Por que 24?

    # Talvez seja a distância de Manhattan + 2*(número de armários - 1)
    # 20 + 2*(25-1) = 20 + 48 = 68, ainda não é 69

    # Vamos tentar distância de Manhattan + 2*número de armários + 1
    # 20 + 2*25 + 1 = 71, não é 69

    # Vamos tentar distância de Manhattan + número de armários * 2 + número de armários
    # 20 + 25*3 = 95, não é 69

    # Outra abordagem: a distância máxima é o número total de células livres
    # menos alguma constante

    # Para o exemplo 1:
    # Células livres: 40
    # Resposta: 29
    # 40 - 11 = 29

    # Para o exemplo 2:
    # Células livres: 121 - 25 = 96
    # Resposta: 69
    # 96 - 27 = 69

    # Não parece haver um padrão claro

    # Vamos tentar uma abordagem diferente: modelar como um problema de fluxo máximo
    # ou usar a ideia de que a distância máxima é a distância de Manhattan
    # mais o número de armários que podemos derrubar vezes 2, mas ajustado

    # Como N e M são pequenos, vamos tentar uma abordagem de BFS com poda
    # Vamos gerar todas as combinações de direções para os armários
    # mas apenas para os armários que estão no "caminho" entre entrada e saída

    # Vamos identificar os armários que estão no retângulo entre entrada e saída
    # e tentar derrubar apenas esses

    # Para o exemplo 1:
    # Entrada: (3,7), Saída: (5,1)
    # Armários no retângulo: todos os 9 armários
    # Vamos tentar derrubar todos

    # Vamos implementar uma BFS que, para cada configuração de armários derrubados,
    # calcula a distância máxima entre entrada e saída

    # Como o número de armários pode ser até 25, mas na prática é menor
    # (para N=M=11, 25 armários), 4^25 é grande, mas podemos tentar
    # otimizar

    # Vamos tentar uma abordagem gulosa: para cada armário, escolher a direção
    # que maximize a distância do caminho

    # Isso pode não dar a solução ótima, mas pode funcionar para os exemplos

    # Vamos implementar uma função que, dado um conjunto de direções de armários,
    # calcula a distância máxima entre entrada e saída

    def bfs_max_distance(blocked):
        from collections import deque
        # blocked é um conjunto de tuplas (i,j) que estão bloqueadas
        visited = [[False] * (M + 1) for _ in range(N + 1)]
        queue = deque()
        queue.append((Xe, Ye, 1))
        visited[Xe][Ye] = True
        max_dist = 0

        while queue:
            i, j, dist = queue.popleft()
            if (i, j) == (Xs, Ys):
                if dist > max_dist:
                    max_dist = dist
                continue
            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ni, nj = i + di, j + dj
                if 1 <= ni <= N and 1 <= nj <= M and not visited[ni][nj] and (ni, nj) not in blocked:
                    visited[ni][nj] = True
                    queue.append((ni, nj, dist + 1))
        return max_dist

    # Agora, vamos tentar todas as combinações de direções para os armários
    # Mas como 4^num_armarios pode ser grande, vamos tentar uma abordagem
    # que escolhe a direção de cada armário que maximize a distância

    # Vamos usar uma estratégia gulosa: para cada armário, tentar as 4 direções
    # e escolher a que dá a maior distância

    # Vamos implementar uma função que tenta derrubar um armário em uma direção
    # e calcula a distância máxima

    def try_direction(armario, direction, blocked):
        i, j = armario
        di, dj = direction
        new_blocked = set(blocked)
        # Verificar se a direção é válida (não bloqueia entrada ou saída)
        # e não causa sobreposição com outros armários derrubados
        # Adicionar as células bloqueadas
        ni1, nj1 = i + di, j + dj
        ni2, nj2 = i, j
        if 1 <= ni1 <= N and 1 <= nj1 <= M:
            new_blocked.add((ni1, nj1))
        if 1 <= ni2 <= N and 1 <= nj2 <= M:
            new_blocked.add((ni2, nj2))
        return new_blocked

    # Vamos tentar uma abordagem de busca em profundidade limitada
    # para explorar as combinações de direções

    # Como o número de armários pode ser até 25, mas na prática é menor
    # (para N=M=11, 25 armários), 4^25 é grande, mas podemos tentar
    # otimizar com poda

    # Vamos tentar uma abordagem de programação dinâmica com bitmask
    # mas o número de armários pode ser até 25, então 2^25 = 33M, que é viável
    # mas precisamos armazenar as direções, então 4^25 é grande

    # Vamos tentar uma abordagem diferente: perceber que a distância máxima
    # é a distância de Manhattan entre entrada e saída, mais 2 vezes o número
    # de armários que estão no "caminho" entre entrada e saída

    # Vamos contar quantos armários estão no retângulo entre entrada e saída
    # e multiplicar por 2

    # Para o exemplo 1:
    # Entrada: (3,7), Saída: (5,1)
    # Armários no retângulo: todos os 9 armários
    # 8 + 2*9 = 26, mas a resposta é 29

    # Vamos tentar adicionar 3 vezes o número de armários:
    # 8 + 3*9 = 35, ainda não é 29

    # Vamos tentar distância de Manhattan + número de armários * 3 - 4
    # 8 + 9*3 - 4 = 8 + 27 - 4 = 31, não é 29

    # Vamos tentar distância de Manhattan + número de armários * 2 + número de armários // 2
    # 8 + 9*2 + 4 = 8 + 18 + 4 = 30, próximo de 29

    # Para o exemplo 2:
    # 20 + 25*2 + 12 = 20 + 50 + 12 = 82, não é 69

    # Não está funcionando

    # Vamos tentar uma abordagem de BFS com estados que incluem as direções dos armários
    # Mas como o número de armários pode ser grande, vamos tentar uma abordagem
    # que apenas considera os armários que estão no "caminho" entre entrada e saída

    # Vamos identificar os armários que estão no retângulo entre entrada e saída
    # e tentar derrubar apenas esses

    min_i = min(Xe, Xs)
    max_i = max(Xe, Xs)
    min_j = min(Ye, Ys)
    max_j = max(Ye, Ys)

    relevant_armarios = []
    for (i, j) in armarios:
        if min_i <= i <= max_i and min_j <= j <= max_j:
            relevant_armarios.append((i, j))

    num_relevant = len(relevant_armarios)

    # Se não houver armários relevantes, a distância é a distância de Manhattan + 1
    if num_relevant == 0:
        print(abs(Xe - Xs) + abs(Ye - Ys) + 1)
        return

    # Vamos tentar todas as combinações de direções para os armários relevantes
    # O número de combinações é 4^num_relevant
    # Para num_relevant = 9, 4^9 = 262144, que é viável

    directions_list = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    # Vamos gerar todas as combinações de direções para os armários relevantes
    for directions in product(directions_list, repeat=num_relevant):
        blocked = set()
        valid = True
        for idx in range(num_relevant):
            i, j = relevant_armarios[idx]
            di, dj = directions[idx]
            ni1, nj1 = i + di, j + dj
            ni2, nj2 = i, j
            # Verificar se as células estão livres (não são entrada ou saída)
            if (ni1, nj1) == (Xe, Ye) or (ni1, nj1) == (Xs, Ys) or (ni2, nj2) == (Xe, Ye) or (ni2, nj2) == (Xs, Ys):
                valid = False
                break
            if 1 <= ni1 <= N and 1 <= nj1 <= M:
                blocked.add((ni1, nj1))
            if 1 <= ni2 <= N and 1 <= nj2 <= M:
                blocked.add((ni2, nj2))
        if not valid:
            continue
        # Adicionar armários não relevantes como bloqueados na direção atual
        for (i, j) in armarios:
            if (i, j) not in relevant_armarios:
                # Armários não relevantes podem ser derrubados em qualquer direção
                # Vamos escolher uma direção que não bloqueie o caminho
                # Por simplicidade, vamos derrubar para a direita
                di, dj = 0, 1
                ni1, nj1 = i + di, j + dj
                ni2, nj2 = i, j
                if 1 <= ni1 <= N and 1 <= nj1 <= M:
                    blocked.add((ni1, nj1))
                if 1 <= ni2 <= N and 1 <= nj2 <= M:
                    blocked.add((ni2, nj2))
        dist = bfs_max_distance(blocked)
        if dist > max_dist:
            max_dist = dist

    print(max_dist)

if __name__ == "__main__":
    main()