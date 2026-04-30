
import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    iterator = iter(input_data)
    test_case = 1
    
    while True:
        try:
            s_str = next(iterator)
        except StopIteration:
            break
        S = int(s_str)
        if S == 0:
            break
            
        X = []
        Y = []
        for _ in range(S):
            X.append(int(next(iterator)))
            Y.append(int(next(iterator)))
            
        X.sort()
        Y.sort()
        
        med_x = X[S // 2]
        med_y = Y[S // 2]
        
        print(f"Teste {test_case}")
        print(f"{med_x} {med_y}")
        print()
        
        test_case += 1

if __name__ == '__main__':
    solve()
