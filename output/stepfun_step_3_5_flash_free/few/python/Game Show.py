import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    s = data[1].strip()
    room = 1
    for c in s:
        if c == 'E':
            room *= 2
        else:
            room = room * 2 + 1
    print(room)

if __name__ == "__main__":
    main()