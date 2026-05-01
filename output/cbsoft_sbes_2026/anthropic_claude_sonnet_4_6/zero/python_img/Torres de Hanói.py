import sys

def hanoi_moves(n):
    return (1 << n) - 1

test_num = 1
for line in sys.stdin:
    n = int(line.strip())
    if n == 0:
        break
    print(f"Teste {test_num}")
    print(hanoi_moves(n))
    print()
    test_num += 1