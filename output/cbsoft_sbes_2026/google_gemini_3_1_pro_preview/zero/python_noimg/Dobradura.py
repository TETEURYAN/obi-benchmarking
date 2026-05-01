import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    teste = 1
    for item in input_data:
        n = int(item)
        if n == -1:
            break
        
        res = (2**n + 1)**2
        print(f"Teste {teste}")
        print(res)
        print()
        teste += 1

if __name__ == '__main__':
    solve()