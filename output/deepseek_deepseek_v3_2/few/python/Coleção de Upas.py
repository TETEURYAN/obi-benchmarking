import sys

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    N = int(next(it))
    M = int(next(it))

    # lista de pares que não combinam
    forbidden = [set() for _ in range(N+1)]
    for _ in range(M):
        u = int(next(it))
        v = int(next(it))
        forbidden[u].add(v)
        forbidden[v].add(u)

    # bitmask de cores escolhidas
    chosen = 0
    # raridade de uma cor i é 2^i, representado por peso = 1<<i
    # podemos pensar como: escolher cores maximizando o maior índice escolhido

    # começar da cor mais alta (maior peso) e tentar incluir
    # porém, não podemos incluir duas cores que não combinam
    # podemos construir um grafo de "combinação" (cores que combinam)
    # o complemento do grafo dado: dois vértices têm uma aresta se eles combinam,
    # i.e., se não estão na lista de forbidden

    # O problema é: escolher um conjunto de vértices que seja um clique no grafo de combinação
    # (todos os vértices escolhidos combinam entre si) e com soma de pesos máxima.

    # Como peso é 2^i, é equivalente a maximizar o maior índice escolhido,
    # pois se você tem um vértice i e outro j com i>j, 2^i >> 2^j.
    # Portanto, intuitivamente, você quer incluir o vértice mais alto possível
    # e depois tentar incluir outros que combinam com ele.

    # Mas a solução exata pode ser complexa. Observando que N, M ≤ 10^5,
    # e que o grafo de combinação pode ser denso, precisamos de abordagem eficiente.

    # Ideia: Começar com conjunto candidato = todas cores (1..N).
    # Para cada cor i de N down to 1, verificar se ela pode ser adicionada ao conjunto atual
    # (i.e., ela não conflita com qualquer cor já escolhida).
    # Se não conflita, adiciona.
    # Isso produzirá um conjunto maximal por inclusão (não podemos adicionar mais cores)
    # Mas será o de máxima soma? Não necessariamente, pois escolher uma cor alta pode impedir
    # muitas outras, e talvez um conjunto menor de cores mais altas seja melhor.

    # Mas note: raridade = 2^i, então se você tem cor i e j (i>j), 2^i > soma de 2^j para muitos j.
    # Exemplo: i=10, 2^10=1024. j=9..1 soma = 1023. Assim, uma única cor alta vale mais que todas menores.
    # Portanto, a estratégia greedy de pegar maior cor possível que não conflita com nenhuma outra já escolhida
    # deve ser correta? Vamos testar com casos.

    # Implementação greedy:
    chosen_set = set()
    # começar da maior cor
    for i in range(N, 0, -1):
        # verifica se i conflita com qualquer já escolhido
        conflict = False
        for c in chosen_set:
            if c in forbidden[i]:
                conflict = True
                break
        if not conflict:
            chosen_set.add(i)

    # resultado
    Q = len(chosen_set)
    colors = sorted(chosen_set)
    print(Q)
    print(*colors)

if __name__ == "__main__":
    solve()