
import sys
import math

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    iterator = iter(input_data)
    test_case = 1
    
    while True:
        try:
            n_str = next(iterator)
        except StopIteration:
            break
        N = int(n_str)
        if N == 0:
            break
            
        pts = []
        for _ in range(N):
            x = int(next(iterator))
            y = int(next(iterator))
            pts.append((x, y))
            
        min_max_sq = float('inf')
        for xi, yi in pts:
            max_sq = max([(xi - xj) * (xi - xj) + (yi - yj) * (yi - yj) for xj, yj in pts])
            if max_sq < min_max_sq:
                min_max_sq = max_sq
                
        ans = math.ceil(2 * math.sqrt(min_max_sq) + 5)
        
        print(f"Teste {test_case}")
        print(ans)
        print()
        
        test_case += 1

if __name__ == '__main__':
    solve()
