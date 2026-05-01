
test_count = 1

while True:
    N = int(input().strip())
    if N == -1:
        break

    if N == 0:
        pieces = 1
    else:
        pieces = (2 ** N + 1) ** 2

    print(f"Teste {test_count}")
    print(pieces)
    print()
    test_count += 1
