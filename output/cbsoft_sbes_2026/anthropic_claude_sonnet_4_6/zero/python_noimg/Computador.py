import sys
from math import sqrt

input = sys.stdin.readline

def main():
    import sys
    data = sys.stdin.read().split()
    idx = 0
    N = int(data[idx]); idx+=1
    M = int(data[idx]); idx+=1
    
    # We need to handle FRENTE and TRÁS efficiently
    # FRENTE i V: mem[j] += V - (j - i) for j in [i, i+V-1] ∩ [1,N]
    #   = mem[j] += (V + i) - j
    # TRÁS i V: mem[j] += V - (i - j) for j in [i-V+1, i] ∩ [1,N]
    #   = mem[j] += (V - i) + j
    
    # For FRENTE: contribution to position p is (V + i) - p if i <= p <= i+V-1
    # For TRÁS: contribution to position p is (V - i) + p if i-V+1 <= p <= i
    
    # We can use difference arrays with lazy evaluation
    # For FRENTE operations: value at p = sum over all frente ops where i <= p <= i+V-1 of (V+i) - p
    #   = sum of (V+i) for qualifying ops - p * count of qualifying ops
    # For TRÁS operations: value at p = sum over all tras ops where i-V+1 <= p <= i of (V-i) + p
    #   = sum of (V-i) for qualifying ops + p * count of qualifying ops
    
    # Use BIT (Fenwick tree) for range updates and point queries
    # For FRENTE: we need two BITs: one for constants (V+i), one for coefficients of p (-1 each)
    # For TRÁS: two BITs: one for constants (V-i), one for coefficients of p (+1 each)
    
    # BIT for range update, point query using difference array approach
    
    size = N + 2
    
    # frente_const: stores sum of (V+i) contributions
    # frente_coef: stores count (coefficient for -p)
    # tras_const: stores sum of (V-i) contributions  
    # tras_coef: stores count (coefficient for +p)
    
    frente_const = [0] * (size + 1)
    frente_coef = [0] * (size + 1)
    tras_const = [0] * (size + 1)
    tras_coef = [0] * (size + 1)
    
    def bit_update(bit, i, val):
        while i <= size:
            bit[i] += val
            i += i & (-i)
    
    def bit_query(bit, i):
        s = 0
        while i > 0:
            s += bit[i]
            i -= i & (-i)
        return s
    
    def range_update(bit, l, r, val):
        bit_update(bit, l, val)
        bit_update(bit, r+1, -val)
    
    def point_query(bit, i):
        return bit_query(bit, i)
    
    out = []
    
    for _ in range(M):
        op = int(data[idx]); idx+=1
        if op == 1:
            i = int(data[idx]); idx+=1
            V = int(data[idx]); idx+=1
            # FRENTE: affects positions [i, min(i+V-1, N)]
            l = i
            r = min(i + V - 1, N)
            if l <= r:
                # contribution to p: (V+i) - p
                range_update(frente_const, l, r, V + i)
                range_update(frente_coef, l, r, 1)
        elif op == 2:
            i = int(data[idx]); idx+=1
            V = int(data[idx]); idx+=1
            # TRÁS: affects positions [max(i-V+1,1), i]
            l = max(i - V + 1, 1)
            r = i
            if l <= r:
                # contribution to p: (V-i) + p
                range_update(tras_const, l, r, V - i)
                range_update(tras_coef, l, r, 1)
        else:
            i = int(data[idx]); idx+=1
            # IMPRIME i
            fc = point_query(frente_const, i)
            fcoef = point_query(frente_coef, i)
            tc = point_query(tras_const, i)
            tcoef = point_query(tras_coef, i)
            val = fc - fcoef * i + tc + tcoef * i
            out.append(val)
    
    print('\n'.join(map(str, out)))

main()