
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    operations = list(map(int, data[1:n+1]))

    a = 0
    b = 0

    for op in operations:
        if op == 1:
            a ^= 1
        elif op == 2:
            a ^= 1
            b ^= 1

    print(a)
    print(b)

if __name__ == "__main__":
    main()
