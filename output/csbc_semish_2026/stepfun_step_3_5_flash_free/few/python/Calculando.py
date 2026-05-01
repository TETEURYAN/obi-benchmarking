import sys

def avaliar(expr):
    i = 0
    n = len(expr)
    num = 0
    while i < n and expr[i].isdigit():
        num = num * 10 + int(expr[i])
        i += 1
    resultado = num
    while i < n:
        op = expr[i]
        i += 1
        num = 0
        while i < n and expr[i].isdigit():
            num = num * 10 + int(expr[i])
            i += 1
        if op == '+':
            resultado += num
        else:
            resultado -= num
    return resultado

def main():
    data = sys.stdin.read().splitlines()
    idx = 0
    teste = 1
    out_lines = []
    while idx < len(data):
        m_line = data[idx].strip()
        if not m_line:
            idx += 1
            continue
        m = int(m_line)
        idx += 1
        if m == 0:
            break
        if idx >= len(data):
            break
        expr = data[idx].strip()
        idx += 1
        res = avaliar(expr)
        out_lines.append(f"Teste {teste}")
        out_lines.append(str(res))
        out_lines.append("")
        teste += 1
    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    main()