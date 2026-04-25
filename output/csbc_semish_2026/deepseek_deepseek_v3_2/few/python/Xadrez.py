import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    L = int(data[0])
    C = int(data[1])
    # (1,1) is white, parity: (row+col) even -> white, odd -> black
    if (L + C) % 2 == 0:
        print(1)
    else:
        print(0)

if __name__ == "__main__":
    main()