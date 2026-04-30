import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    test_number = 1
    for item in input_data:
        n = int(item)
        if n == -1:
            break
        
        ans = (2**n + 1)**2
        print(f"Teste {test_number}")
        print(ans)
        print()
        
        test_number += 1

if __name__ == '__main__':
    solve()