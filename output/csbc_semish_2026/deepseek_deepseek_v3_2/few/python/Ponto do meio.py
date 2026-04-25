import sys

def main():
    data = sys.stdin.read().strip()
    if not data:
        return
    N = int(data)

    # Para N passos, começamos com 4 pontos (vértices do quadrado inicial)
    # A cada passo, para cada quadrado existente, adicionamos:
    # - 4 pontos no meio dos lados
    # - 1 ponto no centro do quadrado
    # Mas pontos podem ser compartilhados entre quadrados.
    # Observando a sequência: passo 0: 4 pontos, passo 1: 9, passo 2: 25.
    # Isso sugere a recorrência: P(n) = 2 * P(n-1) - 1, com P(0) = 4.
    # Verificando: P(1) = 2*4 - 1 = 7? Não bate com 9.
    # Outra observação: os números são quadrados perfeitos: 4=2^2, 9=3^2, 25=5^2.
    # Sequência: 2, 3, 5, ... parece ser a sequência de Fibonacci deslocada: F(n+2) onde F(1)=1, F(2)=1.
    # F(3)=2, F(4)=3, F(5)=5, F(6)=8, F(7)=13...
    # Para n=0 passos: F(4)=3? Não, queremos 2 -> F(3)=2.
    # Para n=1: F(4)=3 -> 3^2=9.
    # Para n=2: F(5)=5 -> 5^2=25.
    # Para n=5: F(8)=21 -> 21^2=441? Mas o exemplo diz 1089, que é 33^2.
    # Então a sequência é: 2, 3, 5, 9, 17, 33,... que é a_n = 2^(n) + 1.
    # Verificando: n=0: 2^0+1=2 -> 2^2=4.
    # n=1: 2^1+1=3 -> 3^2=9.
    # n=2: 2^2+1=5 -> 5^2=25.
    # n=5: 2^5+1=33 -> 33^2=1089. Correto.
    # Portanto, a resposta é (2^N + 1)^2.

    side_points = (1 << N) + 1  # 2^N + 1
    result = side_points * side_points
    print(result)

if __name__ == "__main__":
    main()