
def main():
    n = int(input())
    seq = [int(input()) for _ in range(n)]

    count = 0
    i = 0
    while i < n:
        current = seq[i]
        count += 1
        while i + 1 < n and seq[i + 1] == current:
            i += 1
        i += 1

    print(count)

if __name__ == "__main__":
    main()
