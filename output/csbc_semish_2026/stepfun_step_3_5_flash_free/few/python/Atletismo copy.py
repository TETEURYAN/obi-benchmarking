import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    ordem = list(map(int, data[1:1+n]))
    pos = [0] * (n + 1)
    for i, atleta in enumerate(ordem, start=1):
        pos[atleta] = i
    out_lines = [str(pos[i]) for i in range(1, n+1)]
    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    main()