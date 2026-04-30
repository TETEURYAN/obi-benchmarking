
def main():
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    sequence = list(map(int, data[1:n+1]))

    max_count = 0
    for num1 in range(1, n+1):
        for num2 in range(num1, n+1):
            count = 0
            last = None
            for num in sequence:
                if num == num1 or num == num2:
                    if num != last:
                        count += 1
                        last = num
            if count > max_count:
                max_count = count
    print(max_count)

if __name__ == "__main__":
    main()
