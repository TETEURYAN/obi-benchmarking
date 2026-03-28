import sys

def main():
    t1 = int(sys.stdin.readline())
    t2 = int(sys.stdin.readline())
    t3 = int(sys.stdin.readline())

    times = [(t1, 1), (t2, 2), (t3, 3)]
    times.sort()

    print(times[0][1])
    print(times[1][1])
    print(times[2][1])

if __name__ == "__main__":
    main()