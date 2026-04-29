import sys

def main():
    data = list(map(int, sys.stdin.read().split()))
    if not data:
        return
    n = data[0]
    w = data[1:1+n]

    reachable = {0}
    for x in w:
        new_reachable = set()
        for y in reachable:
            if abs(x - y) <= 8:
                new_reachable.add(x)
        if x <= 8:
            new_reachable.add(x)
        reachable = new_reachable
        if not reachable:
            print("N")
            return

    print("S")

if __name__ == "__main__":
    main()
