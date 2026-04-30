
def main():
    n = int(input())
    sequence = [int(input()) for _ in range(n)]

    count = 1
    last = sequence[0]

    for num in sequence[1:]:
        if num != last:
            count += 1
            last = num

    print(count)

if __name__ == "__main__":
    main()
