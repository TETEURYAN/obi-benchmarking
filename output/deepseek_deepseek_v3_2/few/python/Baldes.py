import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    it = iter(data)
    N = int(next(it))
    M = int(next(it))
    
    buckets = [int(next(it))] * N
    # Mantém a menor e maior bola em cada balde
    min_vals = buckets[:]
    max_vals = buckets[:]
    
    # Para operações tipo 2, precisamos saber o menor e maior valor em todo intervalo [a,b]
    # Isso pode ser feito com segment tree
    # Construir segment trees para min e max
    # Usaremos arrays de tamanho 2*N para representar a segment tree em heap
    size = N
    min_tree = [0] * (2 * size)
    max_tree = [0] * (2 * size)
    
    # Inicializar segment trees
    for i in range(N):
        min_tree[size + i] = buckets[i]
        max_tree[size + i] = buckets[i]
    for i in range(size - 1, 0, -1):
        min_tree[i] = min(min_tree[2 * i], min_tree[2 * i + 1])
        max_tree[i] = max(max_tree[2 * i], max_tree[2 * i + 1])
    
    results = []
    
    for _ in range(M):
        op = int(next(it))
        if op == 1:
            p = int(next(it))
            i = int(next(it)) - 1  # Convertendo para índice 0-based
            # Atualizar o balde i: adicionar bola p
            # Atualizar min_vals[i] e max_vals[i] com p
            min_vals[i] = min(min_vals[i], p)
            max_vals[i] = max(max_vals[i], p)
            # Atualizar segment trees
            idx = size + i
            min_tree[idx] = min_vals[i]
            max_tree[idx] = max_vals[i]
            idx //= 2
            while idx:
                min_tree[idx] = min(min_tree[2 * idx], min_tree[2 * idx + 1])
                max_tree[idx] = max(max_tree[2 * idx], max_tree[2 * idx + 1])
                idx //= 2
        else:
            a = int(next(it)) - 1
            b = int(next(it)) - 1
            # Buscar min e max no intervalo [a, b]
            # Para segment tree, fazemos query de min e max
            # Como a segment tree está em heap, vamos usar funções de query
            left = a + size
            right = b + size
            min_val = float('inf')
            max_val = -float('inf')
            while left <= right:
                if left % 2 == 1:
                    min_val = min(min_val, min_tree[left])
                    max_val = max(max_val, max_tree[left])
                    left += 1
                if right % 2 == 0:
                    min_val = min(min_val, min_tree[right])
                    max_val = max(max_val, max_tree[right])
                    right -= 1
                left //= 2
                right //= 2
            
            # A maior diferença absoluta possível entre duas bolas de baldes distintos no intervalo
            # é a diferença entre o maior valor máximo e o menor valor mínimo de baldes distintos.
            # Ou seja, max_val - min_val (se min_val e max_val vêm de baldes distintos).
            # Se min_val e max_val vierem do mesmo balde, precisamos encontrar o segundo menor ou segundo maior?
            # Não, porque se o min_val e max_val estão no mesmo balde, podemos usar o segundo menor (de outro balde) com o max_val,
            # ou o segundo maior (de outro balde) com o min_val.
            # Mas note: a diferença pode ser entre qualquer duas bolas de baldes distintos.
            # Então basta calcular max_val - min_val, mas se eles vierem do mesmo balde, então a resposta é 0? Não, porque pode haver outro balde.
            # Precisamos do maior e menor de baldes distintos.
            # Solução: temos o global min e max no intervalo. Se eles estão no mesmo balde, então precisamos considerar o segundo menor ou segundo maior.
            # Como a segment tree só guarda o min/max de cada posição, não guarda o segundo.
            # Outra abordagem: para cada balde, temos min e max. Então podemos considerar todos os baldes no intervalo:
            #   menor_val = min(min_vals[i] para i em [a,b])
            #   maior_val = max(max_vals[i] para i em [a,b])
            # Se eles vierem do mesmo balde i, então o menor_val é min_vals[i] e maior_val é max_vals[i].
            # Mas pode haver outro balde j com min_vals[j] muito pequeno ou max_vals[j] muito grande.
            # Portanto, a maior diferença possível seria max(max_vals) - min(min_vals) onde max_vals e min_vals são de baldes diferentes.
            # Se o balde que tem max_vals é o mesmo que tem min_vals, então a resposta é max(max_vals de outros baldes) - min_vals desse balde,
            # ou max_vals desse balde - min(min_vals de outros baldes).
            # Para isso, precisamos saber o segundo maior max_val e o segundo menor min_val no intervalo.
            # Isso pode ser feito com segment tree que guarda tanto o min quanto o max? Não, precisamos de mais informação.
            # Alternativa: podemos manter dois valores: o menor min_val e o maior max_val, e também o segundo menor e segundo maior.
            # Mas isso complica.
            # Observação: a maior diferença será sempre (max de algum balde) - (min de outro balde).
            # Portanto, basta calcular o máximo entre:
            #   1) (max_val de um balde) - (min_val de outro balde)
            # Para isso, podemos pegar o maior max_val e o menor min_val do intervalo. Se eles são do mesmo balde, então tentamos:
            #   maior diferença usando o segundo maior max_val (de outro balde) com o menor min_val,
            #   ou usando o maior max_val com o segundo menor min_val (de outro balde).
            # Portanto, precisamos saber o segundo maior max_val e o segundo menor min_val no intervalo.
            # Como fazer isso eficientemente? Podemos usar duas segment trees: uma para max_val e outra para min_val, mas não para segundo.
            # Uma solução: manter em cada balde uma lista de todas bolas? Não, porque pode ter muitas.
            # Mas o problema diz: cada balde contém inicialmente uma bola, e podemos adicionar bolas (operação tipo 1).
            # Então cada balde pode ter múltiplas bolas. Mas apenas precisamos do menor e maior peso em cada balde.
            # A maior diferença absoluta possível entre duas bolas de baldes distintos: será a diferença entre o maior valor máximo de um balde e o menor valor mínimo de outro balde.
            # Portanto, basta considerar os valores min_vals e max_vals de cada balde.
            # Para o intervalo [a,b], temos listas de min_vals e max_vals.
            # A resposta é max(max_vals[i] - min_vals[j]) para i != j.
            # Isso pode ser calculado como: max(max_vals) - min(min_vals) se os índices são diferentes.
            # Se os índices são o mesmo, então precisamos considerar o segundo maior max_val ou o segundo menor min_val.
            # Para isso, podemos encontrar os dois maiores max_val e os dois menores min_val no intervalo.
            # Vamos fazer isso com segment tree que guarda o maior e segundo maior, e o menor e segundo menor.
            # Mas isso aumenta a complexidade. Alternativa: podemos fazer uma busca linear no intervalo? O intervalo pode ser grande, N=10^5, M=10^5, então não pode.
            # Outra ideia: se o balde que tem o max_val também tem o min_val, então a diferença max_val - min_val não pode ser usada, mas podemos usar max_val - min_val de outro balde, ou max_val de outro balde - min_val.
            # Portanto, a resposta será max(max_val - second_min_val, second_max_val - min_val).
            # Então precisamos do segundo maior max_val e segundo menor min_val.
            # Implementaremos segment tree que para cada nó guarda:
            #   max1, max2 (dois maiores valores)
            #   min1, min2 (dois menores valores)
            # Com isso, podemos fazer query para intervalo [a,b] e obter esses quatro valores.
            # Inicializar: cada balde tem uma bola inicial, então max1 = max_val, max2 = -inf; min1 = min_val, min2 = inf.
            # Quando adicionamos uma bola p, atualizamos:
            #   Se p > max1: max2 = max1, max1 = p
            #   Else if p > max2: max2 = p
            #   Se p < min1: min2 = min1, min1 = p
            #   Else if p < min2: min2 = p
            # Mas isso só considera duas bolas? Cada balde pode ter muitas bolas, mas apenas precisamos das duas maiores e duas menores.
            # Porque a maior diferença entre bolas de baldes distintos será sempre entre uma das maiores bolas e uma das menores bolas (de baldes diferentes).
            # Portanto, manter apenas as duas maiores e duas menores é suficiente.
            # Refazendo a segment tree.
    
    # Reimplementar com segment tree que guarda dois maiores e dois menores.
    
    # Inicializar arrays de duas maiores e duas menores para cada balde
    # Cada balde tem uma bola inicial.
    # Para cada balde, inicialmente:
    #   max1 = valor inicial, max2 = -inf
    #   min1 = valor inicial, min2 = inf
    INF = float('inf')
    max1_list = buckets[:]
    max2_list = [-INF] * N
    min1_list = buckets[:]
    min2_list = [INF] * N
    
    # Segment tree: cada nó guarda max1, max2, min1, min2 para o intervalo que representa.
    # Usaremos 4 arrays de tamanho 2*size.
    max1_tree = [0] * (2 * size)
    max2_tree = [-INF] * (2 * size)
    min1_tree = [0] * (2 * size)
    min2_tree = [INF] * (2 * size)
    
    # Inicializar folhas
    for i in range(N):
        max1_tree[size + i] = buckets[i]
        max2_tree[size + i] = -INF
        min1_tree[size + i] = buckets[i]
        min2_tree[size + i] = INF
    
    # Construir segment tree
    for i in range(size - 1, 0, -1):
        left = 2 * i
        right = 2 * i + 1
        # Combinar max1 e max2
        all_max = [max1_tree[left], max2_tree[left], max1_tree[right], max2_tree[right]]
        all_max.sort(reverse=True)
        max1_tree[i] = all_max[0]
        max2_tree[i] = all_max[1]
        # Combinar min1 e min2
        all_min = [min1_tree[left], min2_tree[left], min1_tree[right], min2_tree[right]]
        all_min.sort()
        min1_tree[i] = all_min[0]
        min2_tree[i] = all_min[1]
    
    # Função para atualizar um balde quando adicionamos uma bola
    def update(pos, p):
        # Atualizar listas locais
        max1_list[pos] = max(max1_list[pos], p)
        # Atualizar max2_list
        if p > max1_list[pos]:
            max2_list[pos] = max1_list[pos]
            max1_list[pos] = p
        elif p > max2_list[pos]:
            max2_list[pos] = p
        
        min1_list[pos] = min(min1_list[pos], p)
        if p < min1_list[pos]:
            min2_list[pos] = min1_list[pos]
            min1_list[pos] = p
        elif p < min2_list[pos]:
            min2_list[pos] = p
        
        # Atualizar segment tree
        idx = size + pos
        max1_tree[idx] = max1_list[pos]
        max2_tree[idx] = max2_list[pos]
        min1_tree[idx] = min1_list[pos]
        min2_tree[idx] = min2_list[pos]
        idx //= 2
        while idx:
            left = 2 * idx
            right = 2 * idx + 1
            all_max = [max1_tree[left], max2_tree[left], max1_tree[right], max2_tree[right]]
            all_max.sort(reverse=True)
            max1_tree[idx] = all_max[0]
            max2_tree[idx] = all_max[1]
            all_min = [min1_tree[left], min2_tree[left], min1_tree[right], min2_tree[right]]
            all_min.sort()
            min1_tree[idx] = all_min[0]
            min2_tree[idx] = all_min[1]
            idx //= 2
    
    # Função para query no intervalo [l, r]
    def query(l, r):
        l += size
        r += size
        # Inicializar listas de valores máximos e mínimos
        all_max = []
        all_min = []
        while l <= r:
            if l % 2 == 1:
                all_max.append(max1_tree[l])
                all_max.append(max2_tree[l])
                all_min.append(min1_tree[l])
                all_min.append(min2_tree[l])
                l += 1
            if r % 2 == 0:
                all_max.append(max1_tree[r])
                all_max.append(max2_tree[r])
                all_min.append(min1_tree[r])
                all_min.append(min2_tree[r])
                r -= 1
            l //= 2
            r //= 2
        
        # Obter os dois maiores valores de all_max
        all_max.sort(reverse=True)
        mx1 = all_max[0]
        mx2 = all_max[1]
        # Obter os dois menores valores de all_min
        all_min.sort()
        mn1 = all_min[0]
        mn2 = all_min[1]
        
        # Calcular a maior diferença possível
        # Se mx1 e mn1 são do mesmo balde, não podemos usar mx1 - mn1.
        # Mas como sabemos se são do mesmo balde? Não sabemos diretamente.
        # Contudo, podemos calcular a resposta como:
        #   max(mx1 - mn2, mx2 - mn1)
        # Isso porque mx1 - mn1 não pode ser usado se são do mesmo balde, então consideramos mx1 com o segundo menor, ou mx2 com o menor.
        # Mas também pode ser mx2 - mn2 se mx1 e mn1 são do mesmo balde e mx2 e mn2 são de outros baldes? Não precisamos, porque mx1 - mn2 ou mx2 - mn1 já cobrem.
        # Portanto, resposta = max(mx1 - mn2, mx2 - mn1)
        # Mas note: se mx2 é -INF ou mn2 é INF, então essa diferença pode ser negativa? Não, porque sempre haverá pelo menos dois baldes no intervalo? 
        # O intervalo [a,b] tem b>=a, mas pode ser apenas um balde? No problema, a operação tipo 2 tem a e b com 1 ≤ a < b ≤ N, então sempre há pelo menos dois baldes.
        # Portanto, há pelo menos dois valores distintos de min e max.
        # Mas se mx2 é -INF, significa que só há um valor máximo distinto? Isso só acontece se todos baldes têm o mesmo máximo? Mas ainda há dois baldes, então mx2 deve ser o segundo maior, que pode ser igual ao maior se todos são iguals? Nesse caso, mx2 = mx1? Mas nós guardamos mx2 como segundo maior, se todos são iguals, mx2 será mx1 também? Na nossa combinação, quando ordenamos, se há valores repetidos, eles aparecem. Exemplo: [10,10,10,10] -> mx1=10, mx2=10.
        # Então mx2 pode ser igual a mx1. Similar para mn2.
        # Portanto, mx1 - mn2 ou mx2 - mn1 podem ser zero se mx1==mx2 e mn1==mn2? Mas ainda é uma diferença válida se são de baldes diferentes? Não sabemos.
        # No entanto, a resposta final deve ser a maior diferença absoluta possível entre duas bolas de baldes distintos. Se mx1 e mn1 são do mesmo balde, então mx1 - mn1 não é válido, mas mx1 - mn2 pode ser válido se mn2 é de outro balde. Se mx1 e mn2 também são do mesmo balde? Então mx2 - mn1.
        # Como nossa query não sabe qual balde forneceu cada valor, assumimos que mx1 e mn1 podem ser do mesmo balde, então calculamos max(mx1 - mn2, mx2 - mn1).
        # Isso deve funcionar.
        ans = max(mx1 - mn2, mx2 - mn1)
        return ans
    
    # Processar operações
    for _ in range(M):
        op = int(next(it))
        if op == 1:
            p = int(next(it))
            i = int(next(it)) - 1
            update(i, p)
        else:
            a = int(next(it)) - 1
            b = int(next(it)) - 1
            ans = query(a, b)
            results.append(ans)
    
    # Imprimir resultados
    sys.stdout.write("\n".join(map(str, results)))

if __name__ == "__main__":
    main()