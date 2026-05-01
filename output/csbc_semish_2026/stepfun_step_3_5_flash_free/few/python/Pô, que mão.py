import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    x = int(data[1])
    y = int(data[2])
    z = int(data[3])
    custos = [x, y, z]
    custos.sort()
    a, b, c = custos
    if a + b + c <= n:
        print(3)
    elif a + b <= n:
        print(2)
    elif a <= n:
        print(1)
    else:
        print(0)

if __name__ == "__main__":
    main()