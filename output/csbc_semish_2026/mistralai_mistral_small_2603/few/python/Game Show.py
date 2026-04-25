
import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    instructions = data[1].strip()
    current = 1
    for move in instructions:
        if move == 'E':
            current *= 2
        else:
            current = current * 2 + 1
    print(current)

if __name__ == "__main__":
    main()
