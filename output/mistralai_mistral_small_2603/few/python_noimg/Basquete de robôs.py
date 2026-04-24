import sys

def main():
    D = int(sys.stdin.read())
    if D <= 800:
        print(1)
    elif D < 1400:
        print(2)
    else:
        print(3)

if __name__ == "__main__":
    main()