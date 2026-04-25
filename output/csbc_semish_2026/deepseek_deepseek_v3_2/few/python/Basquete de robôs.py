import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    D = int(data[0])
    if D <= 800:
        print(1)
    elif D <= 1400:
        print(2)
    else:
        print(3)

if __name__ == "__main__":
    main()