import sys

data = sys.stdin.read().split()
out = []
t = 1
i = 0

while i < len(data):
    m = int(data[i])
    i += 1
    if m == 0:
        break

    expr = data[i]
    i += 1

    total = 0
    num = 0
    op = '+'

    for ch in expr:
        if '0' <= ch <= '9':
            num = num * 10 + (ord(ch) - 48)
        else:
            if op == '+':
                total += num
            else:
                total -= num
            op = ch
            num = 0

    if op == '+':
        total += num
    else:
        total -= num

    out.append(f"Teste {t}")
    out.append(str(total))
    out.append("")
    t += 1

sys.stdout.write("\n".join(out))