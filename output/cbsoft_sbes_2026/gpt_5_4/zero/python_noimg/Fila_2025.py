import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n = data[0]
    a = data[1:1+n]

    max_right = -1
    visible = 0

    for h in reversed(a):
        if h > max_right:
            visible += 1
            max_right = h

    print(n - visible)

if __name__ == "__main__":
    main()
