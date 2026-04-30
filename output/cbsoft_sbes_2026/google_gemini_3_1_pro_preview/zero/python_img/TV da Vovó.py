
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
            row = [next(iterator) for _ in range(N)]
            matrix.append(row)
            
        total_x = 0
        total_y = 0
        
        while True:
            x = int(next(iterator))
            y = int(next(iterator))
            if x == 0 and y == 0:
                break
            total_x += x
            total_y += y
            
        print(f"Teste {test_case}")
        for i in range(M):
            orig_r = (i + total_y) % M
            out_row = [matrix[orig_r][(j - total_x) % N] for j in range(N)]
            print(" ".join(out_row))
        print()
        
        test_case += 1

if __name__ == '__main__':
    solve()
