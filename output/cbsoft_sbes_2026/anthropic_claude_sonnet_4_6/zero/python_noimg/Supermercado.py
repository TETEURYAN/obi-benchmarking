import sys

def solve():
    input_data = sys.stdin.read().split()
    idx = 0
    test_num = 1
    
    while idx < len(input_data):
        S = int(input_data[idx]); idx += 1
        if S == 0:
            break
        
        xs = []
        ys = []
        for _ in range(S):
            x = int(input_data[idx]); idx += 1
            y = int(input_data[idx]); idx += 1
            xs.append(x)
            ys.append(y)
        
        xs.sort()
        ys.sort()
        
        med_x = xs[S // 2] if S % 2 == 1 else xs[(S - 1) // 2]
        med_y = ys[S // 2] if S % 2 == 1 else ys[(S - 1) // 2]
        
        print(f"Teste {test_num}")
        print(f"{med_x} {med_y}")
        print()
        test_num += 1

solve()