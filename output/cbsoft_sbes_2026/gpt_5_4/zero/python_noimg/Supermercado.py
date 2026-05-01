import sys

def median(values):
    values.sort()
    return values[len(values) // 2]

def main():
    data = sys.stdin.read().strip().split()
    i = 0
    test = 1
    out = []

    while i < len(data):
        s = int(data[i])
        i += 1
        if s == 0:
            break

        xs = []
        ys = []
        for _ in range(s):
            x = int(data[i])
            y = int(data[i + 1])
            i += 2
            xs.append(x)
            ys.append(y)

        mx = median(xs)
        my = median(ys)

        out.append(f"Teste {test}")
        out.append(f"{mx} {my}")
        out.append("")
        test += 1

    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()
