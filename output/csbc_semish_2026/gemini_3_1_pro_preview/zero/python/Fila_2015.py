
import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    N = int(data[0])
    A = [int(x) for x in data[1:N+1]]
    Q = int(data[N+1])
    
    offset = N + 2
    num_type_0 = 0
    for q in range(Q):
        if data[offset + 3 * q] == '0':
            num_type_0 += 1
            
    M = N + num_type_0
    if M == 0:
        return
        
    bit = [0] * (M + 1)
    for i in range(1, M + 1):
        bit[i] += 1
        nxt = i + (i & (-i))
        if nxt <= M:
            bit[nxt] += bit[i]
            
    LOG_M = M.bit_length()
    
    final_pos_of_op = [0] * Q
    for q in range(Q - 1, -1, -1):
        if data[offset + 3 * q] == '0':
            k = int(data[offset + 3 * q + 1]) + 1
            pos = 0
            for i in range(LOG_M, -1, -1):
                nxt = pos + (1 << i)
                if nxt <= M and bit[nxt] < k:
                    pos = nxt
                    k -= bit[pos]
            pos += 1
            final_pos_of_op[q] = pos
            
            p = pos
            while p <= M:
                bit[p] -= 1
                p += p & (-p)
                
    initial_positions = [0] * N
    for k in range(1, N + 1):
        pos = 0
        rem_k = k
        for i in range(LOG_M, -1, -1):
            nxt = pos + (1 << i)
            if nxt <= M and bit[nxt] < rem_k:
                pos = nxt
                rem_k -= bit[pos]
        initial_positions[k - 1] = pos + 1
        
    final_height = [0] * (M + 1)
    for k in range(N):
        final_height[initial_positions[k]] = A[k]
        
    for q in range(Q):
        if data[offset + 3 * q] == '0':
            final_height[final_pos_of_op[q]] = int(data[offset + 3 * q + 2])
            
    bit = [0] * (M + 1)
    
    S = 1
    while S <= M:
        S *= 2
    tree = [0] * (2 * S)
    
    for k in range(N):
        pos = initial_positions[k]
        p = pos
        while p <= M:
            bit[p] += 1
            p += p & (-p)
        tree[S + pos - 1] = A[k]
        
    for i in range(S - 1, 0, -1):
        tree[i] = tree[2 * i] if tree[2 * i] > tree[2 * i + 1] else tree[2 * i + 1]
        
    out = []
    for q in range(Q):
        idx_base = offset + 3 * q
        t = data[idx_base]
        if t == '0':
            pos = final_pos_of_op[q]
            p = pos
            while p <= M:
                bit[p] += 1
                p += p & (-p)
            
            idx = S + pos - 1
            tree[idx] = int(data[idx_base + 2])
            idx //= 2
            while idx > 0:
                tree[idx] = tree[2 * idx] if tree[2 * idx] > tree[2 * idx + 1] else tree[2 * idx + 1]
                idx //= 2
        else:
            k = int(data[idx_base + 1])
            pos = 0
            for i in range(LOG_M, -1, -1):
                nxt = pos + (1 << i)
                if nxt <= M and bit[nxt] < k:
                    pos = nxt
                    k -= bit[pos]
            pos += 1
            
            V = final_height[pos] + int(data[idx_base + 2])
            
            if pos == 1:
                out.append('0')
                continue
                
            L = S
            R = S + pos - 2
            left_nodes = []
            right_nodes = []
            while L <= R:
                if L % 2 == 1:
                    left_nodes.append(L)
                    L += 1
                if R % 2 == 0:
                    right_nodes.append(R)
                    R -= 1
                L //= 2
                R //= 2
                
            found_idx = -1
            for node in right_nodes:
                if tree[node] > V:
                    while node < S:
                        if tree[2 * node + 1] > V:
                            node = 2 * node + 1
                        else:
                            node = 2 * node
                    found_idx = node - S
                    break
            if found_idx == -1:
                for i in range(len(left_nodes) - 1, -1, -1):
                    node = left_nodes[i]
                    if tree[node] > V:
                        while node < S:
                            if tree[2 * node + 1] > V:
                                node = 2 * node + 1
                            else:
                                node = 2 * node
                        found_idx = node - S
                        break
                        
            if found_idx == -1:
                out.append('0')
            else:
                p = found_idx + 1
                s = 0
                while p > 0:
                    s += bit[p]
                    p -= p & (-p)
                out.append(str(s))
                
    if out:
        print('\n'.join(out))

if __name__ == '__main__':
    solve()
