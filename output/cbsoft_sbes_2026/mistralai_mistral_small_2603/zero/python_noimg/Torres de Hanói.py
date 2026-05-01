
def hanoi_moves(n):
    return (1 << n) - 1

test_number = 1
while True:
    n = int(input().strip())
    if n == 0:
        break
    print(f"Teste {test_number}")
    print(hanoi_moves(n))
    print()
    test_number += 1
