import sys

data = sys.stdin.read().split()
i = 0
test_num = 1
while i < len(data):
    n = int(data[i])
    if n == -1:
        break
    result = (2**n + 1)**2
    print(f"Teste {test_num}")
    print(result)
    print()
    test_num += 1
    i += 1