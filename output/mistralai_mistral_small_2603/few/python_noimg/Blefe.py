
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return

    n = int(data[0])
    m = int(data[1])
    A = set(map(int, data[2:2+n]))
    B = list(map(int, data[2+n:2+n+m]))

    possible = set()
    possible.update(A)

    for num in B:
        if num in possible:
            possible.add(num * 2)
            possible.add(num + num)
        else:
            print(num)
            return

    print("sim")

if __name__ == "__main__":
    main()
