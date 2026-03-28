import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    N = int(data[0])
    out_lines = []
    for i in range(N):
        line = []
        for j in range(N):
            v = 1 + min(min(i, j), min(N-1-i, N-1-j))
            line.append(str(v))
        out_lines.append(" ".join(line))
    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    main()