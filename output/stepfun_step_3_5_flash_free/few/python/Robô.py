import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    N = int(data[0])
    C = int(data[1])
    S = int(data[2])
    commands = list(map(int, data[3:3+C]))
    
    pos = 0
    count = 0
    if pos == S - 1:
        count += 1
    for cmd in commands:
        if cmd == 1:
            pos = (pos + 1) % N
        else:
            pos = (pos - 1) % N
        if pos == S - 1:
            count += 1
    print(count)

if __name__ == "__main__":
    main()