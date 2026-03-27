import sys

def main():
    data = sys.stdin.read().split()
    N = int(data[0])
    D = int(data[1])
    A = int(data[2])

    if A == D:
        print(0)
        return

    clockwise = (D - A) % N
    counter_clockwise = (A - D) % N

    print(min(clockwise, counter_clockwise))

if __name__ == "__main__":
    main()