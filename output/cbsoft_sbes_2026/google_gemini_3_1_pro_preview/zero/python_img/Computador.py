import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    M = int(input_data[1])
    
    bit_const = [0] * (N + 2)
    bit_x = [0] * (N + 2)
    
    out = []
    idx = 2
    for _ in range(M):
        type = int(input_data[idx])
        if type == 1:
            i = int(input_data[idx+1])
            v = int(input_data[idx+2])
            idx += 3
            
            L = i
            R = i + v - 1
            if R > N:
                R = N
            
            c_val = v + i
            
            curr = L
            while curr <= N:
                bit_const[curr] += c_val
                bit_x[curr] -= 1
                curr += curr & (-curr)
                
            curr = R + 1
            while curr <= N:
                bit_const[curr] -= c_val
                bit_x[curr] += 1
                curr += curr & (-curr)
            
        elif type == 2:
            i = int(input_data[idx+1])
            v = int(input_data[idx+2])
            idx += 3
            
            L = i - v + 1
            if L < 1:
                L = 1
            R = i
            
            c_val = v - i
            
            curr = L
            while curr <= N:
                bit_const[curr] += c_val
                bit_x[curr] += 1
                curr += curr & (-curr)
                
            curr = R + 1
            while curr <= N:
                bit_const[curr] -= c_val
                bit_x[curr] -= 1
                curr += curr & (-curr)
            
        else:
            i = int(input_data[idx+1])
            idx += 2
            
            ans_const = 0
            ans_x = 0
            curr = i
            while curr > 0:
                ans_const += bit_const[curr]
                ans_x += bit_x[curr]
                curr -= curr & (-curr)
                
            out.append(str(ans_const + ans_x * i))
            
    if out:
        sys.stdout.write('\n'.join(out) + '\n')

if __name__ == '__main__':
    solve()