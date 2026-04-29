import sys

def main():
    data = list(map(int, sys.stdin.read().split()))
    if not data:
        return
    n = data[0]
    w = data[1:1+n]
    w.sort()

    i = 0
    j = 0  # first box currently on second floor and available to descend

    while i < n:
        if j < i and w[i] - w[j] <= 8:
            i += 1
            j += 1
        elif w[i] <= 8:
            i += 1
        else:
            print("N")
            return

    print("S")

if __name__ == "__main__":
    main()
