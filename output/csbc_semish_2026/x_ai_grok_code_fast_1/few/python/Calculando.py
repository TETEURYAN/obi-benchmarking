import sys

data = sys.stdin.read().splitlines()
idx = 0
test_num = 1
while True:
    m = int(data[idx])
    idx += 1
    if m == 0:
        break
    expr = data[idx]
    idx += 1
    result = 0
    i = 0
    # Primeiro número
    num = 0
    while i < len(expr) and expr[i].isdigit():
        num = num * 10 + int(expr[i])
        i += 1
    result = num
    # Processar operadores e números restantes
    while i < len(expr):
        op = expr[i]
        i += 1
        num = 0
        while i < len(expr) and expr[i].isdigit():
            num = num * 10 + int(expr[i])
            i += 1
        if op == '+':
            result += num
        elif op == '-':
            result -= num
    print(f"Teste {test_num}")
    print(result)
    print()
    test_num += 1