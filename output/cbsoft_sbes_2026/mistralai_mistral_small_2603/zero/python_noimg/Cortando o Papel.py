
import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    heights = list(map(int, data[1:n+1]))

    max_pieces = 0
    current_pieces = 0
    prev_height = 0

    for h in heights:
        if h > prev_height:
            current_pieces += 1
        elif h < prev_height:
            current_pieces = 1
        else:
            current_pieces += 1
        if current_pieces > max_pieces:
            max_pieces = current_pieces
        prev_height = h

    print(max_pieces)

if __name__ == "__main__":
    main()
