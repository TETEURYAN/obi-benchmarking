import sys

def solve():
    # Leitura rápida de todos os dados de entrada
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    # O primeiro elemento é N
    n = int(input_data[0])
    
    # Os próximos N elementos são os tamanhos dos palitinhos
    # Convertemos para inteiros
    sticks = list(map(int, input_data[1:n+1]))
    
    # Ordenamos os palitinhos. Isso permite o uso da técnica de dois ponteiros
    # e simplifica a verificação da desigualdade triangular.
    sticks.sort()
    
    count = 0
    
    # Iteramos pelo array escolhendo o maior lado do triângulo (k)
    # Começamos do final (maior valor) e vamos até o índice 2 (terceiro menor)
    # pois precisamos de pelo menos 2 elementos menores (i e j) à esquerda.
    for k in range(n - 1, 1, -1):
        i = 0
        j = k - 1
        
        # Para cada k, tentamos encontrar pares (i, j) tal que i < j < k
        # e sticks[i] + sticks[j] > sticks[k]
        while i < j:
            if sticks[i] + sticks[j] > sticks[k]:
                # Se a soma dos menores (i) com o maior dos dois (j) já satisfaz a condição,
                # então qualquer sticks[x] com i <= x < j também satisfará com sticks[j],
                # pois sticks[x] >= sticks[i].
                # Portanto, existem (j - i) triângulos válidos com o lado j e k fixos.
                count += (j - i)
                
                # Reduzimos j para procurar novos pares com o mesmo k
                j -= 1
            else:
                # Se a soma é muito pequena, precisamos aumentar sticks[i].
                # Como o array está ordenado, incrementar i aumenta a soma.
                i += 1
                
    print(count)

if __name__ == "__main__":
    solve()