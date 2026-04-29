import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n = data[0]
    a = data[1:1+n]

    pos = [0] * (n + 1)
    for i, v in enumerate(a, 1):
        pos[v] = i

    rounds = 1
    for x in range(2, n + 1):
        if pos[x] < pos[x - 1]:
            rounds += 1

    print(rounds)

if __name__ == "__main__":
    main()
