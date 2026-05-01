
def main():
    import sys
    input = sys.stdin.read().split()
    ptr = 0
    N = int(input[ptr])
    ptr += 1
    C = int(input[ptr])
    ptr += 1
    S = int(input[ptr])
    ptr += 1
    commands = list(map(int, input[ptr:ptr+C]))
    ptr += C

    current = 1
    count = 0
    if current == S:
        count += 1

    for cmd in commands:
        if cmd == 1:
            current = (current % N) + 1
        else:
            current = (current - 2) % N + 1
        if current == S:
            count += 1

    print(count)

if __name__ == "__main__":
    main()
