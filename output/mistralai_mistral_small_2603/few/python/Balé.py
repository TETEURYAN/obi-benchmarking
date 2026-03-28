import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    levels = list(map(int, data[1:n+1]))

    # Criar lista de tuplas (nível, índice original)
    indexed = [(level, i) for i, level in enumerate(levels)]
    # Ordenar por nível (habilidade) em ordem crescente
    indexed.sort()

    total = 0
    # Para cada bailarina (exceto a última, pois não há quem seja mais habilidosa)
    for j in range(n - 1):
        # A bailarina atual é indexed[j][1] (índice original)
        # Todas as bailarinas com índice > indexed[j][1] são mais antigas (vêm depois na lista original)
        # Precisamos contar quantas dessas têm nível maior que indexed[j][0]
        # Como indexed está ordenado por nível, podemos usar busca binária
        # Mas como queremos contar elementos com índice > current_index, faremos:
        # Percorrer da direita para esquerda no sorted list até encontrar o primeiro com índice <= current_index
        # Ou usar uma estrutura que permita busca eficiente

        # Abordagem: para cada j, contar quantas bailarinas com índice > indexed[j][1] têm nível > indexed[j][0]
        # Como indexed está ordenado por nível, podemos iterar do final para o início
        # Mas isso seria O(n^2) no pior caso (n=1e5 -> 1e10 operações, inviável)

        # Solução eficiente: ordenar por índice e usar Fenwick Tree / BIT ou Segment Tree
        # Ou ordenar por nível e usar dois ponteiros

        # Nova abordagem:
        # Ordenar as bailarinas por nível (já feito)
        # Para cada bailarina i (em ordem de nível crescente), queremos contar quantas bailarinas j com:
        #   nível[j] > nível[i] E índice[j] > índice[i]
        # Isso é equivalente a: para cada i, contar o número de elementos à direita de i no array original
        # que têm nível maior que levels[i]

        # Podemos processar da direita para esquerda no array original, mantendo uma estrutura que permita
        # consultar quantos elementos já vistos têm nível maior que o atual

        # Vamos reordenar nossa estratégia:
        pass

    # Solução correta:
    # Precisamos contar pares (i, j) onde:
    #   levels[i] < levels[j] E i < j
    # Mas com a restrição adicional de que a mais habilidosa deve ser a mais antiga
    # Ou seja, se levels[i] < levels[j], então i deve ser > j (porque quem tem nível maior é mais habilidosa,
    # e quem tem índice maior na lista original é mais antiga)
    # Portanto, queremos pares (i, j) onde:
    #   levels[i] < levels[j] E i > j

    # Ou seja, para cada par de índices (j, i) com j < i, queremos levels[j] < levels[i]
    # Mas isso contaria todos os pares onde a mais antiga tem nível menor que a mais nova
    # O problema quer o contrário: a mais habilidosa (nível maior) deve ser a mais antiga (índice maior)
    # Portanto, queremos pares (i, j) onde:
    #   levels[i] > levels[j] E i < j

    # Reinterpretando o exemplo:
    # Input: [1, 5, 2, 4, 3] (índices 0,1,2,3,4)
    # Pares válidos: (5,2), (5,4), (5,3), (4,3)
    # Em termos de índices:
    #   (1,2): levels[1]=5 > levels[2]=2 e 1<2 -> válido
    #   (1,3): levels[1]=5 > levels[3]=4 e 1<3 -> válido
    #   (1,4): levels[1]=5 > levels[4]=3 e 1<4 -> válido
    #   (3,4): levels[3]=4 > levels[4]=3 e 3<4 -> válido
    # Total: 4

    # Portanto, o problema se reduz a: contar o número de inversões onde o elemento à esquerda é maior
    # que o elemento à direita, ou seja, contar pares (i, j) com i < j e levels[i] > levels[j]

    # Mas atenção: o problema diz que a bailarina que exemplifica deve ser a mais habilidosa E a mais antiga
    # No par (i,j) onde i < j (i é mais antigo, j é mais novo):
    #   - A mais habilidosa é max(levels[i], levels[j])
    #   - A mais antiga é i (porque i < j)
    # Para satisfazer a condição, precisamos que:
    #   max(levels[i], levels[j]) == levels[i] E i < j
    # Isso implica levels[i] > levels[j]

    # Portanto, queremos exatamente contar o número de pares (i, j) com i < j e levels[i] > levels[j]

    # Isso é o número de inversões no array!

    # Mas atenção: o problema diz "o total de pares válidos, em todos os casos, será < 1 000 000"
    # Isso sugere que podemos usar um algoritmo O(n^2) em casos médios, mas n=1e5 requer O(n log n)

    # Portanto, usaremos um algoritmo para contar inversões com complexidade O(n log n)

    # Implementação com Merge Sort modificado para contar inversões

    def count_inversions(arr):
        if len(arr) <= 1:
            return arr, 0

        mid = len(arr) // 2
        left, inv_left = count_inversions(arr[:mid])
        right, inv_right = count_inversions(arr[mid:])
        merged, inv_merge = merge_and_count(left, right)

        total_inv = inv_left + inv_right + inv_merge
        return merged, total_inv

    def merge_and_count(left, right):
        result = []
        i = j = 0
        inv_count = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
                inv_count += len(left) - i

        result.extend(left[i:])
        result.extend(right[j:])
        return result, inv_count

    # Mas note: nosso array original é levels = [1,5,2,4,3]
    # Queremos contar pares (i,j) com i<j e levels[i] > levels[j]
    # No array [1,5,2,4,3]:
    #   (5,2), (5,4), (5,3), (4,3) -> 4 inversões

    # Portanto, podemos contar as inversões diretamente no array levels

    _, inversions = count_inversions(levels)
    print(inversions)

if __name__ == "__main__":
    main()