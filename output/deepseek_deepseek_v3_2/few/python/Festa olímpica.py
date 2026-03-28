import sys

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    N = int(next(it))
    M = int(next(it))
    T = [int(next(it)) for _ in range(M)]

    # Remove duplicatas e ordena, pois a ordem dos turnos importa
    # Mas se um número se repete, só a primeira ocorrência importa
    # (turnos subsequentes com mesmo T não removem nada novo)
    seen = set()
    unique_T = []
    for t in T:
        if t not in seen:
            seen.add(t)
            unique_T.append(t)
    M = len(unique_T)

    # Se M == 0, todos são convidados
    if M == 0:
        limit = min(N, 10000)
        for i in range(1, limit + 1):
            print(i)
        return

    # Fase 1: Simulação para N pequeno (até 2*10^5)
    # Isso cobre muitos casos onde N é moderado
    if N <= 200000:
        survivors = list(range(1, N + 1))
        for t in unique_T:
            new_survivors = []
            for idx, val in enumerate(survivors, start=1):
                if idx % t != 0:
                    new_survivors.append(val)
            survivors = new_survivors
            if not survivors:
                break
        limit = min(len(survivors), 10000)
        for i in range(limit):
            print(survivors[i])
        return

    # Fase 2: N grande, usar abordagem matemática
    # A posição final de um número x pode ser calculada
    # Inversamente, podemos achar os primeiros 10000 números que sobrevivem

    # Função que dado um número x, retorna se ele sobrevive
    def survives(x):
        pos = x  # posição inicial
        for t in unique_T:
            if pos % t == 0:
                return False
            # Nova posição = pos - floor(pos / t)
            pos -= pos // t
        return True

    # Busca binária para encontrar o k-ésimo sobrevivente
    def kth_survivor(k):
        # k é 1-indexado
        lo, hi = 1, N
        while lo < hi:
            mid = (lo + hi) // 2
            # Contar quantos sobreviventes <= mid
            cnt = 0
            pos = mid
            for t in unique_T:
                cnt += pos // t
                pos -= pos // t
            survivors_up_to_mid = mid - cnt
            if survivors_up_to_mid >= k:
                hi = mid
            else:
                lo = mid + 1
        return lo

    # Encontrar quantos sobreviventes totais existem
    # Podemos estimar ou calcular exatamente
    pos = N
    for t in unique_T:
        pos -= pos // t
    total_survivors = pos

    limit = min(total_survivors, 10000)
    for k in range(1, limit + 1):
        print(kth_survivor(k))

if __name__ == "__main__":
    solve()