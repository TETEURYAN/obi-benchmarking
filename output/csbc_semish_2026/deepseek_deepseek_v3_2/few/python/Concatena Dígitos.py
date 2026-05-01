import sys

def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    N = int(next(it))
    Q = int(next(it))
    
    digits = [int(next(it)) for _ in range(N)]
    
    # Prefix sums
    prefix_sum = [0] * (N + 1)
    prefix_sum_sq = [0] * (N + 1)
    for i in range(1, N + 1):
        d = digits[i - 1]
        prefix_sum[i] = prefix_sum[i - 1] + d
        prefix_sum_sq[i] = prefix_sum_sq[i - 1] + d * d
    
    out_lines = []
    for _ in range(Q):
        L = int(next(it))
        R = int(next(it))
        length = R - L + 1
        if length < 2:
            out_lines.append('0')
            continue
        
        total_sum = prefix_sum[R] - prefix_sum[L - 1]
        total_sq = prefix_sum_sq[R] - prefix_sum_sq[L - 1]
        
        # Soma de todos os pares (i != j): (10*a_i + a_j)
        # = 10 * (soma de todos os a_i * (length-1)) + (soma de todos os a_j * (length-1))
        # Mas cada par (i,j) com i != j aparece duas vezes? Não, a ordem importa.
        # Para cada i (como dezena): contribuição = a_i * 10 * (length-1)
        # Para cada j (como unidade): contribuição = a_j * (length-1)
        # Total = 10 * total_sum * (length-1) + total_sum * (length-1)
        # = (10 + 1) * total_sum * (length-1) = 11 * total_sum * (length-1)
        # Mas isso conta cada par (i,j) com i != j exatamente uma vez? Sim.
        
        # Verificação: para lista [a,b,c], pares ordenados (i!=j):
        # (a,b): 10a+b, (a,c): 10a+c, (b,a): 10b+a, (b,c): 10b+c, (c,a): 10c+a, (c,b): 10c+b
        # Soma = 10a*(2) + a*(2) + 10b*(2) + b*(2) + 10c*(2) + c*(2) = (10+1)*2*(a+b+c) = 22*(a+b+c)
        # Fórmula: 11 * total_sum * (length-1) = 11 * (a+b+c) * 2 = 22*(a+b+c) ✓
        
        result = 11 * total_sum * (length - 1)
        out_lines.append(str(result))
    
    sys.stdout.write('\n'.join(out_lines))

if __name__ == "__main__":
    main()