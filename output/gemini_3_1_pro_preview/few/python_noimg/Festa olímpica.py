import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    M = int(input_data[1])
    
    T_minus_1 = [int(x) - 1 for x in input_data[M+1:1:-1]]
    
    out = []
    append = out.append
    for p in range(1, 10001):
        if p > N:
            break
        curr = p
        for tm1 in T_minus_1:
            if curr > tm1:
                curr += (curr - 1) // tm1
                if curr > N:
                    break
        if curr > N:
            break
        append(str(curr))
        
    sys.stdout.write('\n'.join(out) + '\n')

solve()