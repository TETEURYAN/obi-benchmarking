import sys

def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    N = int(next(it))
    X1 = int(next(it))
    X2 = int(next(it))
    
    lines = []
    for _ in range(N):
        A = int(next(it))
        B = int(next(it))
        lines.append((A, B))
    
    # Ordenar por A (inclinação) e depois por B
    lines.sort()
    
    # Para cada par de linhas i < j, a interseção x = (Bj - Bi) / (Ai - Aj)
    # Como Ai != Aj para i != j (pois linhas são distintas e ordenadas por A, então Ai <= Aj)
    # Se Ai == Aj, elas são paralelas e não se intersectam.
    # Queremos contar pares (i, j) com i < j tais que X1 <= (Bj - Bi) / (Ai - Aj) <= X2
    
    # Reescrevendo: X1 <= (Bj - Bi) / (Ai - Aj) <= X2
    # Como Ai - Aj < 0 (pois Ai < Aj após ordenação), multiplicar inverte desigualdades.
    # Para Ai < Aj:
    # X1 <= (Bj - Bi) / (Ai - Aj) <= X2
    # Equivalente a:
    # (Bj - Bi) >= X1 * (Ai - Aj)  e  (Bj - Bi) <= X2 * (Ai - Aj)
    # Mas (Ai - Aj) < 0, então:
    # (Bj - Bi) >= X1 * (Ai - Aj)  ->  Bj - Bi <= X1 * (Aj - Ai)   [inverte]
    # (Bj - Bi) <= X2 * (Ai - Aj)  ->  Bj - Bi >= X2 * (Aj - Ai)   [inverte]
    # Portanto, para Ai < Aj:
    # X2 * (Aj - Ai) <= (Bj - Bi) <= X1 * (Aj - Ai)
    
    # Definimos para cada linha i: valor1 = Bi - X1 * Ai, valor2 = Bi - X2 * Ai
    # A condição acima se torna:
    # Para i < j, Ai < Aj:
    # Bj - Bi >= X2 * (Aj - Ai)  ->  Bj - X2 * Aj >= Bi - X2 * Ai  ->  valor2_j >= valor2_i
    # Bj - Bi <= X1 * (Aj - Ai)  ->  Bj - X1 * Aj <= Bi - X1 * Ai  ->  valor1_j <= valor1_i
    
    # Portanto, para cada par (i, j) com i < j e Ai < Aj, a interseção está em [X1, X2] se:
    # valor2_j >= valor2_i  E  valor1_j <= valor1_i
    
    # Isso é equivalente a contar pares (i, j) com i < j tais que:
    # (valor2_i, valor1_i) e (valor2_j, valor1_j) satisfazem valor2_j >= valor2_i e valor1_j <= valor1_i.
    # Isso é um problema de contagem de pares em uma ordem parcial.
    
    # Podemos resolver com uma árvore de Fenwick (BIT) após compressão de coordenadas.
    
    # Calcular valor1 e valor2 para cada linha
    vals1 = []
    vals2 = []
    for A, B in lines:
        v1 = B - X1 * A
        v2 = B - X2 * A
        vals1.append(v1)
        vals2.append(v2)
    
    # Compressão de coordenadas para valor2
    unique_v2 = sorted(set(vals2))
    v2_to_idx = {v: i+1 for i, v in enumerate(unique_v2)}  # BIT indexa a partir de 1
    m = len(unique_v2)
    
    # Ordenar linhas por valor1 decrescente, e para empates, por valor2 crescente?
    # Queremos processar de forma que para cada i, contamos j > i com valor2_j >= valor2_i.
    # Se ordenarmos por valor1 decrescente, então para cada elemento processado, todos os anteriores
    # têm valor1 maior ou igual (portanto valor1_j <= valor1_i é falso se valor1_j > valor1_i?).
    # Precisamos ajustar.
    
    # Reescrevendo a condição: valor1_j <= valor1_i e valor2_j >= valor2_i.
    # Ordenamos por valor1 crescente. Ao processar na ordem crescente de valor1, para cada i,
    # todos os j processados antes têm valor1_j <= valor1_i. Então a condição valor1_j <= valor1_i é satisfeita.
    # Agora precisamos contar dentre esses j quantos têm valor2_j >= valor2_i.
    # Isso é uma contagem inversa: para cada i, contar j < i com valor2_j >= valor2_i.
    # Podemos usar BIT para contar quantos j têm valor2_j <= algum limite? Melhor transformar.
    
    # Invertemos a ordem de valor2: definimos novo_valor2 = -valor2.
    # Então valor2_j >= valor2_i  <=>  novo_valor2_j <= novo_valor2_i.
    # Agora a condição se torna: valor1_j <= valor1_i e novo_valor2_j <= novo_valor2_i.
    # Isso é um problema de contagem de pares em uma ordem 2D: pontos (valor1, novo_valor2).
    # Queremos contar pares (i, j) com i < j tais que ponto i domina ponto j (ambas coordenadas menores ou iguais).
    # Mas cuidado: i < j na ordem de processamento, mas a condição é simétrica? Não, é i < j original.
    # Como estamos ordenando por valor1 crescente, i < j na ordem ordenada implica valor1_i <= valor1_j.
    # Para ter valor1_j <= valor1_i, precisamos que valor1_i == valor1_j. Mas isso não é garantido.
    # Portanto, a abordagem de ordenar por valor1 não funciona diretamente.
    
    # Alternativa: usar transformação geométrica.
    # A interseção entre linha i e j está em [X1, X2] se:
    # (Bi - X1 * Ai) >= (Bj - X1 * Aj)  e  (Bi - X2 * Ai) <= (Bj - X2 * Aj)
    # Ou seja, ponto (Ai, Bi) domina ponto (Aj, Bj) após transformação?
    # Definindo f1(A,B) = B - X1 * A, f2(A,B) = B - X2 * A.
    # Condição: f1(i) >= f1(j) e f2(i) <= f2(j).
    # Isso é equivalente a: (-f1(i), f2(i)) <= (-f1(j), f2(j)) (coordenada a coordenada).
    # Portanto, podemos considerar pontos P_i = (-f1(i), f2(i)) e queremos contar pares i < j tais que P_i <= P_j.
    # Isso é contagem de pares em ordem 2D.
    
    # Calculamos para cada linha:
    # p = - (B - X1 * A) = X1 * A - B
    # q = B - X2 * A
    # Queremos contar pares (i, j) com i < j tais que p_i <= p_j e q_i <= q_j.
    
    # Ordenamos por p crescente, e para empates, por q crescente.
    # Então para cada i, todos os j > i têm p_j >= p_i. Precisamos contar quantos têm q_j >= q_i.
    # Isso é contagem de inversões? Na verdade, queremos contar j > i com q_j >= q_i.
    # Podemos usar BIT para contar quantos q_j <= q_i? Não, queremos >=.
    # Invertemos q: seja r = -q. Então q_j >= q_i  <=>  r_j <= r_i.
    # Agora, ordenando por p crescente, para cada i, contamos j < i com r_j <= r_i.
    # Isso é uma contagem direta com BIT.
    
    # Mas cuidado: a condição original é para i < j (na ordem original das linhas).
    # Como estamos reordenando, perdemos a ordem original. No entanto, a condição é simétrica:
    # se (i,j) satisfaz, então (j,i) também satisfaz? Não, porque a interseção é a mesma.
    # Estamos contando cada interseção uma vez? Sim, porque consideramos pares ordenados i < j.
    # Após reordenar, cada par (i,j) com i < j na nova ordem pode corresponder a um par original
    # com i < j ou j < i. Mas a condição p_i <= p_j e q_i <= q_j é simétrica? Não, porque
    # se p_i <= p_j e q_i <= q_j, então o par (i,j) na nova ordem satisfaz. Se o par original
    # era (j,i) com j < i, então após reordenar, i vem antes de j? Não, porque ordenamos por p.
    # Portanto, cada par de linhas será contado exatamente uma vez se satisfizer a condição,
    # independente da ordem original.
    
    # Vamos implementar essa abordagem.
    
    points = []
    for A, B in lines:
        p = X1 * A - B
        q = B - X2 * A
        points.append((p, q))
    
    # Ordenar por p crescente, e para empates, por q crescente
    points.sort(key=lambda x: (x[0], x[1]))
    
    # Compressão de coordenadas para r = -q
    r_vals = [-q for _, q in points]
    unique_r = sorted(set(r_vals))
    r_to_idx = {v: i+1 for i, v in enumerate(unique_r)}
    bit_size = len(unique_r)
    
    # BIT (Fenwick Tree)
    class Fenwick:
        def __init__(self, n):
            self.n = n
            self.bit = [0] * (n + 2)
        def update(self, idx, delta):
            while idx <= self.n:
                self.bit[idx] += delta
                idx += idx & -idx
        def query(self, idx):
            s = 0
            while idx > 0:
                s += self.bit[idx]
                idx -= idx & -idx
            return s
    
    bit = Fenwick(bit_size)
    total = 0
    for p, q in points:
        r = -q
        idx = r_to_idx[r]
        # Contar quantos pontos anteriores têm r' <= r (ou seja, q' >= q)
        count = bit.query(idx)
        total += count
        bit.update(idx, 1)
    
    print(total)

if __name__ == "__main__":
    main()