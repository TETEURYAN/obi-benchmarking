
def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    n = int(data[0])
    coordinates = set()
    duplicate = False
    index = 1
    for _ in range(n):
        x = int(data[index])
        y = int(data[index + 1])
        index += 2
        if (x, y) in coordinates:
            duplicate = True
            break
        coordinates.add((x, y))
    print(1 if duplicate else 0)

if __name__ == "__main__":
    main()
