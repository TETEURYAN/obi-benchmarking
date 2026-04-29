import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return

    n = int(data[0])
    x = list(map(int, data[1:1 + n]))

    h = max(x)
    out = []

    for level in range(h, 0, -1):
        row = ['1' if xi >= level else '0' for xi in x]
        out.append(' '.join(row))

    sys.stdout.write('\n'.join(out))

if __name__ == "__main__":
    main()
