import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    Q = int(input_data[1])
    
    row_val = [0] * (N + 1)
    row_time = [0] * (N + 1)
    col_val = [0] * (N + 1)
    col_time = [0] * (N + 1)
    
    total_row = [0] * 51
    total_col = [0] * 51
    
    bit_row = [0] * (51 * (Q + 1))
    bit_col = [0] * (51 * (Q + 1))
    
    idx = 2
    out = []
    
    counts = [0] * 51
    
    for t in range(1, Q + 1):
        type = int(input_data[idx])
        if type == 1:
            X = int(input_data[idx+1])
            R = int(input_data[idx+2])
            idx += 3
            
            old_t = row_time[X]
            if old_t > 0:
                old_v = row_val[X]
                total_row[old_v] -= 1
                i = old_t
                offset = old_v * (Q + 1)
                while i <= Q:
                    bit_row[offset + i] -= 1
                    i += i & -i
            
            total_row[R] += 1
            i = t
            offset = R * (Q + 1)
            while i <= Q:
                bit_row[offset + i] += 1
                i += i & -i
                
            row_time[X] = t
            row_val[X] = R
            
        elif type == 2:
            X = int(input_data[idx+1])
            R = int(input_data[idx+2])
            idx += 3
            
            old_t = col_time[X]
            if old_t > 0:
                old_v = col_val[X]
                total_col[old_v] -= 1
                i = old_t
                offset = old_v * (Q + 1)
                while i <= Q:
                    bit_col[offset + i] -= 1
                    i += i & -i
            
            total_col[R] += 1
            i = t
            offset = R * (Q + 1)
            while i <= Q:
                bit_col[offset + i] += 1
                i += i & -i
                
            col_time[X] = t
            col_val[X] = R
            
        elif type == 3:
            X = int(input_data[idx+1])
            idx += 2
            
            r_time = row_time[X]
            r_val = row_val[X]
            
            S = 0
            for v in range(51):
                tot = total_col[v]
                if tot > 0:
                    s = 0
                    i = r_time
                    offset = v * (Q + 1)
                    while i > 0:
                        s += bit_col[offset + i]
                        i -= i & -i
                    c = tot - s
                    counts[v] = c
                    S += c
                else:
                    counts[v] = 0
            
            counts[r_val] += N - S
            
            max_c = -1
            ans = -1
            for v in range(51):
                if counts[v] >= max_c:
                    max_c = counts[v]
                    ans = v
            out.append(str(ans))
            
        else:
            X = int(input_data[idx+1])
            idx += 2
            
            c_time = col_time[X]
            c_val = col_val[X]
            
            S = 0
            for v in range(51):
                tot = total_row[v]
                if tot > 0:
                    s = 0
                    i = c_time
                    offset = v * (Q + 1)
                    while i > 0:
                        s += bit_row[offset + i]
                        i -= i & -i
                    c = tot - s
                    counts[v] = c
                    S += c
                else:
                    counts[v] = 0
            
            counts[c_val] += N - S
            
            max_c = -1
            ans = -1
            for v in range(51):
                if counts[v] >= max_c:
                    max_c = counts[v]
                    ans = v
            out.append(str(ans))

    if out:
        sys.stdout.write('\n'.join(out) + '\n')

if __name__ == '__main__':
    solve()