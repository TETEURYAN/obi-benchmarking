
def main():
    N = int(input().strip())
    if N == 0:
        print(4)
    else:
        total = 4
        for step in range(1, N + 1):
            new_points = 4 * (2 ** (step - 1)) * 5
            total += new_points
        print(total)

if __name__ == "__main__":
    main()
