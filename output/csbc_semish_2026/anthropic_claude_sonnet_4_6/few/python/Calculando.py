import sys

data = sys.stdin.read().splitlines()
i = 0
test_num = 0
results = []

while i < len(data):
    line = data[i].strip()
    i += 1
    if not line:
        continue
    m = int(line)
    if m == 0:
        break
    expr = data[i].strip()
    i += 1
    test_num += 1
    result = eval(expr)
    results.append(f"Teste {test_num}\n{result}\n")

print('\n'.join(results))