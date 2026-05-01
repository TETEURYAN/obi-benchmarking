import sys
from sys import stdin

def main():
    input = stdin.readline
    data = sys.stdin.buffer.read().split()
    idx = 0
    N = int(data[idx]); idx+=1
    M = int(data[idx]); idx+=1
    
    # We need to handle FRENTE and TRAS efficiently
    # FRENTE i V: mem[j] += V - (j - i) for j in [i, i+V-1] ∩ [1,N]
    #   = mem[j] += (V + i) - j
    # TRAS i V: mem[j] += V - (i - j) for j in [i-V+1, i] ∩ [1,N]
    #   = mem[j] += (V - i) + j
    
    # For FRENTE i V: contribution to position j is max(0, V - (j-i)) = V+i - j
    # This is a linear function of j: coefficient of j is -1, constant is V+i
    # Valid for j in [i, min(N, i+V-1)]
    
    # For TRAS i V: contribution to position j is max(0, V - (i-j)) = V-i + j
    # This is a linear function of j: coefficient of j is +1, constant is V-i
    # Valid for j in [max(1, i-V+1), i]
    
    # We can use difference arrays for the linear functions.
    # For a range [l, r] where contribution is a*j + b:
    # We need to query point j.
    
    # Use two BITs (Fenwick trees) to handle range updates of linear functions.
    # For each update on range [l,r] with f(j) = a*j + b:
    # We store coefficients such that prefix sums give us the answer.
    
    # Actually, let's use a different approach:
    # We maintain two arrays A and B such that value at position j = A_prefix[j] * j + B_prefix[j]
    # Using difference arrays for A and B.
    
    # For range [l, r] add (a*j + b):
    # diff_a[l] += a, diff_a[r+1] -= a
    # diff_b[l] += b, diff_b[r+1] -= b
    # Then prefix sum of diff_a gives coefficient, prefix sum of diff_b gives constant.
    # Value at j = (prefix_a[j]) * j + (prefix_b[j])
    # But we need prefix sums up to j, so we need Fenwick trees for point queries with range updates.
    
    # Fenwick tree for range update, point query
    # Update [l,r] += val: bit[l] += val, bit[r+1] -= val
    # Query j: prefix sum [1..j]
    
    size = N + 2
    bit_a = [0] * (size + 2)
    bit_b = [0] * (size + 2)
    
    def update(bit, i, val):
        while i <= size:
            bit[i] += val
            i += i & (-i)
    
    def query(bit, i):
        s = 0
        while i > 0:
            s += bit[i]
            i -= i & (-i)
        return s
    
    def range_update(bit, l, r, val):
        update(bit, l, val)
        if r + 1 <= size:
            update(bit, r + 1, -val)
    
    out = []
    for _ in range(M):
        op = int(data[idx]); idx+=1
        if op == 1:
            i = int(data[idx]); idx+=1
            V = int(data[idx]); idx+=1
            # FRENTE: j in [i, min(N, i+V-1)], add (V+i - j) = -j + (V+i)
            l = i
            r = min(N, i + V - 1)
            # a = -1, b = V+i
            range_update(bit_a, l, r, -1)
            range_update(bit_b, l, r, V + i)
        elif op == 2:
            i = int(data[idx]); idx+=1
            V = int(data[idx]); idx+=1
            # TRAS: j in [max(1, i-V+1), i], add (V-i + j) = j + (V-i)
            l = max(1, i - V + 1)
            r = i
            # a = 1, b = V-i
            range_update(bit_a, l, r, 1)
            range_update(bit_b, l, r, V - i)
        else:
            i = int(data[idx]); idx+=1
            a = query(bit_a, i)
            b = query(bit_b, i)
            out.append(a * i + b)
    
    sys.stdout.write('\n'.join(map(str, out)) + '\n')

main()