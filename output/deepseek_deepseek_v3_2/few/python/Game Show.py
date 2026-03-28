import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    n = int(data[0])
    s = data[1]
    pos = 1
    for c in s:
        if c == 'E':
            pos = 2 * pos
        else:  # c == 'D'
            pos = 2 * pos + 1
    print(pos)

if __name__ == "__main__":
    main()