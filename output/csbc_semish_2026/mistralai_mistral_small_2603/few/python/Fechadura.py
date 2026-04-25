
import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    m = int(data[1])
    pins = list(map(int, data[2:2+n]))

    moves = 0
    for i in range(n - 1):
        diff = m - pins[i]
        pins[i] += diff
        pins[i+1] += diff
        moves += abs(diff)

    print(moves)

if __name__ == "__main__":
    main()
