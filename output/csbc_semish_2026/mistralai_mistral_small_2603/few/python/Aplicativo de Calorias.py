import sys

def main():
    data = sys.stdin.read().split()
    e1 = int(data[0])
    e2 = int(data[1])
    e3 = int(data[2])
    x = int(data[3])

    if e2 - e1 <= x:
        print(e2)
    else:
        print(e3)

if __name__ == "__main__":
    main()