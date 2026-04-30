
def main():
    N = int(input().strip())
    for i in range(N):
        for j in range(N):
            min_val = min(i, j, N - 1 - i, N - 1 - j)
            print(min_val + 1, end=' ')
        print()

if __name__ == '__main__':
    main()
