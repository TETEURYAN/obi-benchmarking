
def main():
    N = int(input().strip())
    if N == 0:
        print(1)
    else:
        total = (N + 1) * (N + 2) // 2
        print(total)

if __name__ == "__main__":
    main()
