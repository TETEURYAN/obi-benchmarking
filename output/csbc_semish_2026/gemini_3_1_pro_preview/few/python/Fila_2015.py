import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    Q = int(input_data[N+1])
    
    K = sum(1 for i in range(Q) if input_data[N + 2 + 3 * i] == '0')
    M = N + K
    
    if M == 0:
        return

    bit_empty = [0] * (M + 1)
    for i in range(1, M + 1):
        bit_empty[i] += 1
        nxt = i + (i & -i)
        if nxt <= M:
            bit_empty[nxt] += bit_empty[i]
            
    op_final_pos = [0] * Q
    is_empty = [True] * (M + 1)
    
    for i in range(Q - 1, -1, -1):
        idx = N + 2 + 3 * i
        if input_data[idx] == '0':
            I_val = int(input_data[idx+1])
            k = I_val + 1
            pos = 0
            for j in range(20, -1, -1):
                next_idx = pos + (1 << j)
                if next_idx <= M and bit_empty[next_idx] < k:
                    pos = next_idx
                    k -= bit_empty[pos]
            pos += 1
            op_final_pos[i] = pos
            is_empty[pos] = False
            
            curr = pos
            while curr <= M:
                bit_empty[curr] -= 1
                curr += curr & -curr
                
    initial_final_pos = [i for i in range(1, M + 1) if is_empty[i]]
    
    bit_active = [0] * (M + 1)
    
    size = 1
    while size < M:
        size *= 2
        
    tree = [0] * (2 * size)
    
    for i in range(N):
        pos = initial_final_pos[i]
        curr = pos
        while curr <= M:
            bit_active[curr] += 1
            curr += curr & -curr
        
        node = (pos - 1) + size
        tree[node] = int(input_data[1 + i])
        node //= 2
        while node > 0:
            tree[node] = tree[2 * node] if tree[2 * node] > tree[2 * node + 1] else tree[2 * node + 1]
            node //= 2
            
    out = []
    for i in range(Q):
        idx = N + 2 + 3 * i
        if input_data[idx] == '0':
            pos = op_final_pos[i]
            curr = pos
            while curr <= M:
                bit_active[curr] += 1
                curr += curr & -curr
            
            X_val = int(input_data[idx+2])
            node = (pos - 1) + size
            tree[node] = X_val
            node //= 2
            while node > 0:
                tree[node] = tree[2 * node] if tree[2 * node] > tree[2 * node + 1] else tree[2 * node + 1]
                node //= 2
        else:
            I_val = int(input_data[idx+1])
            k = I_val
            P = 0
            for j in range(20, -1, -1):
                next_idx = P + (1 << j)
                if next_idx <= M and bit_active[next_idx] < k:
                    P = next_idx
                    k -= bit_active[P]
            P += 1
            
            X_val = int(input_data[idx+2])
            target = tree[(P - 1) + size] + X_val
            
            R = P - 2
            ans_pos = 0
            if R >= 0:
                node = R + size
                if tree[node] > target:
                    ans_pos = R + 1
                else:
                    while True:
                        while node > 1 and node % 2 == 0:
                            node //= 2
                        if node == 1:
                            break
                        node -= 1
                        if tree[node] > target:
                            while node < size:
                                if tree[2 * node + 1] > target:
                                    node = 2 * node + 1
                                else:
                                    node = 2 * node
                            ans_pos = (node - size) + 1
                            break
                        node //= 2
                        
            if ans_pos == 0:
                out.append(0)
            else:
                s = 0
                curr = ans_pos
                while curr > 0:
                    s += bit_active[curr]
                    curr -= curr & -curr
                out.append(s)
                
    if out:
        sys.stdout.write('\n'.join(map(str, out)) + '\n')

if __name__ == '__main__':
    solve()