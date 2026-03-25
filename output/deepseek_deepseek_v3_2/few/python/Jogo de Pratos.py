import sys

MOD = 10**9 + 7

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    it = iter(data)
    
    N = int(next(it))
    M = int(next(it))
    K = int(next(it))
    
    a_spells = [int(next(it)) for _ in range(N)]
    b_spells = [int(next(it)) for _ in range(N)]
    a_meals = [int(next(it)) for _ in range(M)]
    b_meals = [int(next(it)) for _ in range(M)]
    Q = int(next(it))
    queries = [int(next(it)) for _ in range(Q)]
    
    # 1. Processar feitiços: queremos o efeito de usar K vezes o melhor feitiço
    #    O melhor feitiço é aquele que maximiza a transformação após muitas repetições.
    #    Para x grande, o feitiço com maior 'a' domina.
    #    Se 'a' igual, maior 'b' é melhor.
    best_a = 0
    best_b = 0
    for a, b in zip(a_spells, b_spells):
        if a > best_a or (a == best_a and b > best_b):
            best_a = a
            best_b = b
    
    # 2. Calcular o efeito de aplicar o melhor feitiço K vezes:
    #    f(x) = a*x + b
    #    f^n(x) = a^n * x + b * (a^(n-1) + a^(n-2) + ... + 1)
    #           = a^n * x + b * (a^n - 1) // (a - 1)   se a != 1
    #    Se a == 1: f^n(x) = x + n*b
    if K == 0:
        spell_mul = 1
        spell_add = 0
    else:
        if best_a == 1:
            spell_mul = 1
            spell_add = (best_b * (K % MOD)) % MOD
        else:
            # Calcular a^K mod MOD e (a^K - 1) * inv(a-1) mod MOD
            a_mod = best_a % MOD
            pow_aK = pow(a_mod, K, MOD)
            spell_mul = pow_aK
            inv_denom = pow((best_a - 1) % MOD, MOD - 2, MOD)
            spell_add = (best_b % MOD) * ((pow_aK - 1) * inv_denom % MOD) % MOD
    
    # 3. Processar refeições: queremos a composição de todas as refeições em alguma ordem.
    #    A ordem ótima é ordenar por b/(a-1) decrescente (prova via exchange argument).
    #    Mas como M pode ser 10^5, precisamos pré‑computar a composição total.
    meals = list(zip(a_meals, b_meals))
    meals.sort(key=lambda p: p[1] * (p[0] - 1))  # equivalente a b/(a-1) crescente
    # Vamos compor da esquerda para a direita após ordenar.
    total_mul = 1
    total_add = 0
    for a, b in meals:
        total_mul = (total_mul * (a % MOD)) % MOD
        total_add = (total_add * (a % MOD) + (b % MOD)) % MOD
    
    # 4. Composição final: primeiro feitiços, depois refeições.
    #    Seja F(x) = spell_mul * x + spell_add
    #        G(x) = total_mul * x + total_add
    #    Queremos G(F(x)) = total_mul * (spell_mul * x + spell_add) + total_add
    #                     = (total_mul * spell_mul) * x + (total_mul * spell_add + total_add)
    final_mul = (total_mul * spell_mul) % MOD
    final_add = (total_mul * spell_add + total_add) % MOD
    
    # 5. Responder queries
    out_lines = []
    for x in queries:
        res = (final_mul * (x % MOD) + final_add) % MOD
        out_lines.append(str(res))
    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    solve()