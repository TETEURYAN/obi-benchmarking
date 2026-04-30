
def main():
    A, B, C = map(int, input().split())
    X, Y, Z = map(int, input().split())

    max_x = X // A
    max_y = Y // B
    max_z = Z // C

    total = max_x * max_y * max_z
    print(total)

if __name__ == "__main__":
    main()
