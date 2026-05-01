
import sys

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
        n = int(n_str)
        if n == 0:
            break
            
        max_x = -20000
        min_y = 20000
        min_u = 20000
        max_v = -20000
        
        for _ in range(n):
            x = int(next(iterator))
            y = int(next(iterator))
            u = int(next(iterator))
            v = int(next(iterator))
            
            if x > max_x: max_x = x
            if y < min_y: min_y = y
            if u < min_u: min_u = u
            if v > max_v: max_v = v
            
        print(f"Teste {test_case}")
        if max_x >= min_u or min_y <= max_v:
            print("nenhum")
        else:
            print(f"{max_x} {min_y} {min_u} {max_v}")
        print()
        
        test_case += 1

if __name__ == '__main__':
    solve()
