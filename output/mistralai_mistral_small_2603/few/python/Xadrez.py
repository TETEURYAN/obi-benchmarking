import sys

def main():
    data = sys.stdin.read().split()
    L = int(data[0])
    C = int(data[1])
    if (L + C) % 2 == 0:
        print(1)
    else:
        print(0)

if __name__ == "__main__":
    main()