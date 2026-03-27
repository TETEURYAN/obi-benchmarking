
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    m = int(data[1])
    figurinhas = set()
    idx = 2
    for _ in range(m):
        x = int(data[idx])
        idx += 1
        figurinhas.add(x)
    faltam = n - len(figurinhas)
    print(faltam)

if __name__ == "__main__":
    main()
