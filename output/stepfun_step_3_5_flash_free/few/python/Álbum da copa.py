import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    m = int(data[1])
    stickers = set()
    for i in range(2, 2 + m):
        stickers.add(int(data[i]))
    print(n - len(stickers))

if __name__ == "__main__":
    main()