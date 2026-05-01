import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    idx = 0
    test_case = 1
    
    while idx < len(input_data):
        S = int(input_data[idx])
        idx += 1
        if S == 0:
            break
        
        X = []
        Y = []
        for _ in range(S):
            X.append(int(input_data[idx]))
            Y.append(int(input_data[idx+1]))
            idx += 2
            
        X.sort()
        Y.sort()
        
        med_X = X[S // 2]
        med_Y = Y[S // 2]
        
        print(f"Teste {test_case}")
        print(f"{med_X} {med_Y}")
        print()
        
        test_case += 1

if __name__ == '__main__':
    solve()