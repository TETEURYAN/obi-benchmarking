import sys

def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    N = int(data[idx]); idx += 1
    Q = int(data[idx]); idx += 1
    
    # For each row: store (last_assigned_value, last_assigned_time)
    # row_assign[i] = (value, time) or None if never assigned
    row_assign = [None] * (N + 1)  # row_assign[x] = (R, time)
    col_assign = [None] * (N + 1)  # col_assign[x] = (R, time)
    
    # For query type 3 (row X):
    # The row X has N cells. Each cell j is determined by:
    #   - if col_assign[j] exists and col_assign[j].time > row_assign[X].time => col_assign[j].value
    #   - else => row_assign[X].value (or 0 if never assigned)
    # 
    # For query type 4 (col X):
    # The col X has N cells. Each cell i is determined by:
    #   - if row_assign[i] exists and row_assign[i].time > col_assign[X].time => row_assign[i].value
    #   - else => col_assign[X].value (or 0 if never assigned)
    
    # R can be 0..50, so we can count frequencies efficiently
    
    out = []
    time = 0
    
    for _ in range(Q):
        op = int(data[idx]); idx += 1
        
        if op == 1:
            X = int(data[idx]); idx += 1
            R = int(data[idx]); idx += 1
            time += 1
            row_assign[X] = (R, time)
        
        elif op == 2:
            X = int(data[idx]); idx += 1
            R = int(data[idx]); idx += 1
            time += 1
            col_assign[X] = (R, time)
        
        elif op == 3:
            X = int(data[idx]); idx += 1
            # Query row X
            # row base value and time
            if row_assign[X] is None:
                row_val = 0
                row_time = -1
            else:
                row_val, row_time = row_assign[X]
            
            # Count frequencies
            # For each column j (1..N):
            #   if col_assign[j] is not None and col_assign[j][1] > row_time => col_assign[j][0]
            #   else => row_val
            
            # We need to count how many columns have col_assign with time > row_time
            # and group by their value, plus count remaining as row_val
            
            freq = [0] * 51
            
            # Count columns that override row
            override_count = 0
            for j in range(1, N + 1):
                if col_assign[j] is not None and col_assign[j][1] > row_time:
                    freq[col_assign[j][0]] += 1
                    override_count += 1
            
            # Remaining columns use row_val
            freq[row_val] += (N - override_count)
            
            # Find max frequency, tie-break by largest value
            best_val = 0
            best_freq = -1
            for v in range(51):
                if freq[v] > best_freq or (freq[v] == best_freq and v > best_val):
                    best_freq = freq[v]
                    best_val = v
            
            out.append(best_val)
        
        else:  # op == 4
            X = int(data[idx]); idx += 1
            # Query col X
            if col_assign[X] is None:
                col_val = 0
                col_time = -1
            else:
                col_val, col_time = col_assign[X]
            
            freq = [0] * 51
            
            override_count = 0
            for i in range(1, N + 1):
                if row_assign[i] is not None and row_assign[i][1] > col_time:
                    freq[row_assign[i][0]] += 1
                    override_count += 1
            
            freq[col_val] += (N - override_count)
            
            best_val = 0
            best_freq = -1
            for v in range(51):
                if freq[v] > best_freq or (freq[v] == best_freq and v > best_val):
                    best_freq = freq[v]
                    best_val = v
            
            out.append(best_val)
    
    sys.stdout.write('\n'.join(map(str, out)) + ('\n' if out else ''))

main()