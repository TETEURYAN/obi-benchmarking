
def main():
    N = int(input().strip())
    for i in range(N):
        for j in range(N):
            x = min(i, j, N - 1 - i, N - 1 - j) + 1
            print(x, end=' ')
        print()

if __name__ == '__main__':
    main()
