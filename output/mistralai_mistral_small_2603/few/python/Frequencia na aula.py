
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        print(0)
        return
    n = int(data[0])
    if n == 0:
        print(0)
        return
    registros = list(map(int, data[1:n+1]))
    freq = set()
    for num in registros:
        freq.add(num)
    print(len(freq))

if __name__ == "__main__":
    main()
