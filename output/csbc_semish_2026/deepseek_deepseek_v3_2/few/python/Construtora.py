import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    n = int(data[0])
    a = list(map(int, data[1:1+n]))

    # O problema é equivalente a contar o número de operações necessárias
    # para igualar todos os prédios ao maior valor.
    # Cada operação aumenta um segmento contíguo de prédios de mesma altura.
    # Isso se reduz a somar as diferenças entre alturas consecutivas
    # quando a altura aumenta da esquerda para a direita.
    # Formalmente: resposta = soma de max(0, a[i] - a[i-1]) para i de 1 a n-1.

    ans = 0
    for i in range(1, n):
        if a[i] > a[i-1]:
            ans += a[i] - a[i-1]
    # Além disso, precisamos considerar o primeiro prédio:
    # qualquer altura inicial do primeiro prédio precisa ser aumentada
    # até o máximo global, e isso é capturado pela diferença entre
    # o máximo e o primeiro elemento, mas na fórmula acima já está incluso?
    # Vamos pensar: a fórmula acima só captura aumentos locais.
    # Na verdade, a resposta correta é: soma de max(0, a[i] - a[i-1]) para i=1..n-1
    # mais a diferença entre o máximo global e o último elemento? Não.
    # A resposta é simplesmente a soma das diferenças positivas entre consecutivos.
    # Isso porque cada "degrau" ascendente precisa ser preenchido.
    # Testando com os exemplos:
    # Exemplo 1: [3,1,1,2] -> diferenças: -2,0,1 -> soma positivos = 1, mas a saída é 2.
    # Então a fórmula acima está incompleta.
    # Precisamos de uma abordagem diferente.

    # Observação: O problema é conhecido como "Minimum number of operations to make array equal"
    # com a operação de aumentar um segmento contíguo de valores iguais.
    # A solução ótima é: resposta = soma de (a[i] - min_left) onde min_left é o mínimo à esquerda.
    # Mas isso também não parece bater.

    # Vamos pensar de outra forma:
    # A operação permite aumentar um segmento contíguo de prédios com mesma altura.
    # Isso é equivalente a construir a "parede" de andares camada por camada.
    # Podemos pensar em processar da esquerda para a direita e manter a altura atual.
    # Sempre que encontrarmos um prédio mais alto que o anterior, precisamos de operações extras.
    # A resposta é a soma das diferenças entre alturas consecutivas quando a[i] > a[i-1].
    # Mas no exemplo 1: a = [3,1,1,2]
    # diferenças: 3->1 (negativo, ignora), 1->1 (0), 1->2 (1) -> soma = 1, mas resposta esperada 2.
    # Por que? Porque para aumentar o prédio 4 de 1 para 2, precisamos que ele esteja em um segmento
    # com altura 1. Os prédios 2 e 3 têm altura 1, mas o prédio 1 tem altura 3, então não podemos
    # incluir o prédio 1. Portanto, aumentamos os prédios 2,3,4 juntos de 1 para 2 (1 operação).
    # Depois, para igualar todos ao máximo (3), precisamos aumentar os prédios 2,3,4 de 2 para 3
    # (mais 1 operação). Total 2.
    # A fórmula correta é: resposta = soma de max(0, a[i] - a[i-1]) para i=1..n-1, MAS
    # também precisamos considerar a altura inicial do primeiro prédio em relação aos outros?
    # Na verdade, a resposta é a soma das diferenças entre cada prédio e o mínimo à sua esquerda?
    # Vamos testar com o exemplo 1:
    # Para i=0: min_left = infinito? Não.
    # Melhor: resposta = a[0] + soma de max(0, a[i] - a[i-1]) para i=1..n-1? Teste:
    # a[0]=3, soma diferenças positivas=1 -> total=4 (errado).

    # Após pesquisa mental: a solução conhecida é:
    # Seja m = max(a). Para cada posição i, considere a altura atual após algumas operações.
    # A resposta é a soma das "subidas" da sequência, ou seja, soma de max(0, a[i] - a[i-1]).
    # Mas isso deu 1 no exemplo 1, e precisamos de 2.
    # A diferença é que no exemplo 1, o primeiro prédio já está mais alto, então precisamos
    # "baixá-lo"? Não, não podemos baixar. Então como igualar? Temos que aumentar os outros até 3.
    # Para aumentar o prédio 4 de 1 para 3, precisamos de 2 operações (1->2 e 2->3).
    # Mas o prédio 2 e 3 também precisam ser aumentados. Eles podem ser aumentados junto com o 4.
    # Então as operações são:
    # 1) Aumentar prédios 2,3,4 de 1 para 2.
    # 2) Aumentar prédios 2,3,4 de 2 para 3.
    # Total 2. Isso corresponde a: (max - a[1]) = 3-1=2.
    # Mas e o prédio 1? Ele já está no máximo.
    # Então a resposta seria max(a) - min(a)? No exemplo 1: 3-1=2 (correto).
    # Exemplo 2: max=7, min=4, diferença=3, mas a saída é 4. Então não é simplesmente isso.

    # Vamos para uma solução garantida:
    # N <= 100, a_i <= 100. Podemos simular o processo de forma gulosa.
    # A ideia: enquanto não todos iguais, encontre o menor valor entre os prédios que não estão no máximo.
    # Aumente todos os segmentos contíguos com esse valor.
    # Isso é O(N * max(a)) que é 100*100 = 10^4, tranquilo.

    # Implementação simulada:
    target = max(a)
    ans = 0
    current = a[:]
    while True:
        if all(x == target for x in current):
            break
        # Encontrar o menor valor que não é o target
        min_val = target
        for x in current:
            if x < target and x < min_val:
                min_val = x
        # Aumentar todos os segmentos contíguos com valor min_val
        i = 0
        while i < n:
            if current[i] == min_val:
                j = i
                while j < n and current[j] == min_val:
                    j += 1
                # segmento [i, j-1]
                ans += 1
                for k in range(i, j):
                    current[k] += 1
                i = j
            else:
                i += 1
    print(ans)

if __name__ == "__main__":
    solve()