import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return

    A = int(data[0])
    N = int(data[1])
    fluxes = list(map(int, data[2:2+N]))

    count = 0
    threshold = 40000000
    for F in fluxes:
        if F * A >= threshold:
            count += 1

    print(count)

if __name__ == "__main__":
    main()