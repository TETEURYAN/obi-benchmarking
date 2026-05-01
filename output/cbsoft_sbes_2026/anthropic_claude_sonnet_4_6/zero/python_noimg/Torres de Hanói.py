import sys

def solve():
    input_data = sys.stdin.read().split()
    test_num = 1
    for token in input_data:
        n = int(token)
        if n == 0:
            break
        moves = (2 ** n) - 1
        print(f"Teste {test_num}")
        print(moves)
        print()
        test_num += 1

solve()