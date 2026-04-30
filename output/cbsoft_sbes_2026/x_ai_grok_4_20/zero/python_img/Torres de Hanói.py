
import sys

def hanoi_moves(n):
    if n == 0:
        return 0
    return (1 << n) - 1

test_num = 1
for line in sys.stdin:
    n = int(line.strip())
    if n == 0:
        break
    moves = hanoi_moves(n)
    print(f"Teste {test_num}")
    print(moves)
    print()
    test_num += 1
