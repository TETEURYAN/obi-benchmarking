
import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    cartas = list(map(int, data[1:1+n]))

    pos = [0] * (n + 1)
    for i in range(n):
        pos[cartas[i]] = i

    rodadas = 1
    max_pos = pos[1]
    for i in range(2, n + 1):
        if pos[i] < max_pos:
            rodadas += 1
        else:
            max_pos = pos[i]

    print(rodadas)

if __name__ == "__main__":
    main()
