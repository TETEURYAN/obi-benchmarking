import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        print(0)
        return

    n = int(data[0])
    x = int(data[1])
    y = int(data[2])
    z = int(data[3])

    count = 0
    if n >= x:
        count += 1
        n -= x
    if n >= y:
        count += 1
        n -= y
    if n >= z:
        count += 1

    print(count)

if __name__ == "__main__":
    main()