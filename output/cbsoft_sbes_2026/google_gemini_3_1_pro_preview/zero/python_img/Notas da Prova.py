import sys

def main():
    try:
        n = int(sys.stdin.read().strip())
        if n == 0:
            print("E")
        elif n <= 35:
            print("D")
        elif n <= 60:
            print("C")
        elif n <= 85:
            print("B")
        else:
            print("A")
    except ValueError:
        pass

if __name__ == '__main__':
    main()