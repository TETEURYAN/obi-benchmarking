import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    J, P, V, E, D = map(int, data)

    # Função para verificar se todos os valores são consistentes
    def check(J, P, V, E, D):
        return (J == V + E + D) and (P == 3 * V + E)

    # Se já está completo e correto, imprime
    if J != -1 and P != -1 and V != -1 and E != -1 and D != -1:
        if check(J, P, V, E, D):
            print(J, P, V, E, D)
            return

    # Casos com um valor faltando
    # 1) J faltando
    if J == -1:
        if V != -1 and E != -1 and D != -1:
            J = V + E + D
        elif P != -1 and V != -1 and E != -1:
            # P = 3V + E, mas não dá J diretamente
            # Precisamos de D
            if D != -1:
                J = V + E + D
            else:
                # D = J - V - E, mas J desconhecido
                # Não podemos determinar J sem D
                pass
        elif P != -1 and V != -1 and D != -1:
            # P = 3V + E → E = P - 3V
            E = P - 3 * V
            J = V + E + D
        elif P != -1 and E != -1 and D != -1:
            # P = 3V + E → V = (P - E) // 3
            V = (P - E) // 3
            J = V + E + D

    # 2) P faltando
    if P == -1:
        if V != -1 and E != -1:
            P = 3 * V + E

    # 3) V faltando
    if V == -1:
        if P != -1 and E != -1:
            V = (P - E) // 3
        elif J != -1 and E != -1 and D != -1:
            V = J - E - D

    # 4) E faltando
    if E == -1:
        if P != -1 and V != -1:
            E = P - 3 * V
        elif J != -1 and V != -1 and D != -1:
            E = J - V - D

    # 5) D faltando
    if D == -1:
        if J != -1 and V != -1 and E != -1:
            D = J - V - E

    # Casos com dois valores faltando
    # Precisamos resolver o sistema:
    # J = V + E + D   (1)
    # P = 3V + E      (2)

    # Lista de faltantes
    missing = []
    if J == -1:
        missing.append('J')
    if P == -1:
        missing.append('P')
    if V == -1:
        missing.append('V')
    if E == -1:
        missing.append('E')
    if D == -1:
        missing.append('D')

    if len(missing) == 2:
        # Caso 1: faltam J e P
        if 'J' in missing and 'P' in missing:
            if V != -1 and E != -1 and D != -1:
                J = V + E + D
                P = 3 * V + E
        # Caso 2: faltam J e V
        elif 'J' in missing and 'V' in missing:
            if P != -1 and E != -1 and D != -1:
                V = (P - E) // 3
                J = V + E + D
        # Caso 3: faltam J e E
        elif 'J' in missing and 'E' in missing:
            if P != -1 and V != -1 and D != -1:
                E = P - 3 * V
                J = V + E + D
        # Caso 4: faltam J e D
        elif 'J' in missing and 'D' in missing:
            if P != -1 and V != -1 and E != -1:
                D = (P - 3 * V)  # Isso está errado, vamos calcular corretamente
                # Na verdade, temos E = P - 3V, e J = V + E + D → D = J - V - E, mas J não temos
                # Precisamos de outra abordagem: temos V, E, mas falta J e D.
                # Sabemos que J = V + E + D, mas não temos J nem D.
                # Mas temos P = 3V + E, então E = P - 3V.
                # Ainda faltam duas incógnitas J e D.
                # Mas note que D = J - V - E, então J = D + V + E.
                # Isso não resolve. No entanto, o problema garante que há solução.
                # Vamos usar a restrição de que V, E, D são inteiros não negativos.
                # Podemos iterar D de 0 a 100 (limite do problema) e verificar se J = V + E + D
                # e se J está dentro dos limites (1 a 100). Mas isso é força bruta.
                # Como os limites são pequenos (até 100), podemos fazer isso.
                E = P - 3 * V
                for D_try in range(101):
                    J_try = V + E + D_try
                    if 1 <= J_try <= 100:
                        J, D = J_try, D_try
                        break
        # Caso 5: faltam P e V
        elif 'P' in missing and 'V' in missing:
            if J != -1 and E != -1 and D != -1:
                V = J - E - D
                P = 3 * V + E
        # Caso 6: faltam P e E
        elif 'P' in missing and 'E' in missing:
            if J != -1 and V != -1 and D != -1:
                E = J - V - D
                P = 3 * V + E
        # Caso 7: faltam P e D
        elif 'P' in missing and 'D' in missing:
            if J != -1 and V != -1 and E != -1:
                D = J - V - E
                P = 3 * V + E
        # Caso 8: faltam V e E
        elif 'V' in missing and 'E' in missing:
            if J != -1 and P != -1 and D != -1:
                # Sistema:
                # V + E = J - D   (de J = V + E + D)
                # 3V + E = P
                # Subtraindo: (3V + E) - (V + E) = P - (J - D)
                # 2V = P - J + D
                # V = (P - J + D) // 2
                # E = J - D - V
                V = (P - J + D) // 2
                E = J - D - V
        # Caso 9: faltam V e D
        elif 'V' in missing and 'D' in missing:
            if J != -1 and P != -1 and E != -1:
                # J = V + E + D → V + D = J - E
                # P = 3V + E → V = (P - E) // 3
                V = (P - E) // 3
                D = J - E - V
        # Caso 10: faltam E e D
        elif 'E' in missing and 'D' in missing:
            if J != -1 and P != -1 and V != -1:
                # J = V + E + D → E + D = J - V
                # P = 3V + E → E = P - 3V
                E = P - 3 * V
                D = J - V - E

    # Verificação final e impressão
    print(J, P, V, E, D)

if __name__ == "__main__":
    solve()