import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return

    n = int(data[0])
    pos = data[1]
    moves = list(map(int, data[2:2+n]))

    for move in moves:
        if move == 1:
            if pos == 'A':
                pos = 'B'
            elif pos == 'B':
                pos = 'A'
        elif move == 2:
            if pos == 'B':
                pos = 'C'
            elif pos == 'C':
                pos = 'B'
        elif move == 3:
            if pos == 'A':
                pos = 'C'
            elif pos == 'C':
                pos = 'A'

    print(pos)

if __name__ == "__main__":
    main()