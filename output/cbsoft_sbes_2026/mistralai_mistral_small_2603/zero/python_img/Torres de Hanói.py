
def hanoi_moves(n):
    return (1 << n) - 1

test_count = 1
while True:
    n = int(input().strip())
    if n == 0:
        break
    print(f"Teste {test_count}")
    print(hanoi_moves(n))
    print()
    test_count += 1
