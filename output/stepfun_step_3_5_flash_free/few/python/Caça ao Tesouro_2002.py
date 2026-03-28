import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    idx = 0
    teste_num = 1
    out_lines = []
    while idx < len(data):
        x = int(data[idx]); y = int(data[idx+1]); n = int(data[idx+2])
        idx += 3
        if x == 0 and y == 0 and n == 0:
            break
        valores = []
        for _ in range(n):
            valores.append(int(data[idx]))
            idx += 1
        T = sum(valores)
        S = x + y + T
        if S % 2 != 0:
            resultado = 'N'
        else:
            K = S // 2 - x
            if K < 0 or K > T:
                resultado = 'N'
            else:
                if n == 0:
                    resultado = 'S' if K == 0 else 'N'
                else:
                    bits = 1
                    for v in valores:
                        bits = bits | (bits << v)
                    resultado = 'S' if (bits >> K) & 1 else 'N'
        out_lines.append(f"Teste {teste_num}")
        out_lines.append(resultado)
        out_lines.append("")
        teste_num += 1
    print("\n".join(out_lines))

if __name__ == "__main__":
    main()