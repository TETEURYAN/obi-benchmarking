
import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    iterator = iter(input_data)
    
    test_case = 1
    while True:
        try:
            m_str = next(iterator)
            n_str = next(iterator)
        except StopIteration:
            break
            
        M = int(m_str)
        N = int(n_str)
        
        if M == 0 and N == 0:
            break
            
        matrix = []
        for _ in range(M):
            row = []
            for _ in range(N):
                row.append(next(iterator))
            matrix.append(row)
            
        total_X = 0
        total_Y = 0
        
        while True:
            x = int(next(iterator))
            y = int(next(iterator))
            if x == 0 and y == 0:
                break
            total_X += x
            total_Y += y
            
        print(f"Teste {test_case}")
        shift_c = (-total_X) % N
        for r in range(M):
            orig_r = (r + total_Y) % M
            row_out = matrix[orig_r][shift_c:] + matrix[orig_r][:shift_c]
            print(" ".join(row_out))
        print()
        
        test_case += 1

if __name__ == '__main__':
    solve()
