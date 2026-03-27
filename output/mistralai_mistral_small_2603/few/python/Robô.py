
import sys

def main():
    data = sys.stdin.read().split()
    N = int(data[0])
    C = int(data[1])
    S = int(data[2])
    commands = list(map(int, data[3:3+C]))

    current = 1
    count = 0

    if current == S:
        count += 1

    for cmd in commands:
        if cmd == 1:
            current = current + 1
            if current > N:
                current = 1
        else:
            current = current - 1
            if current < 1:
                current = N
        if current == S:
            count += 1

    print(count)

if __name__ == "__main__":
    main()
