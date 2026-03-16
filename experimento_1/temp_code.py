import sys
def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    E = int(data[0])
    D = int(data[1])
    if E > D:
        result = E + D
    else:
        result = 2 * (D - E)
    print(result)
if __name__ == '__main__':
    main()
