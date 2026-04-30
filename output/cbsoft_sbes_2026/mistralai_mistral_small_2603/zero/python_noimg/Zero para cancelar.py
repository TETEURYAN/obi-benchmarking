
def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    n = int(data[0])
    numbers = list(map(int, data[1:n+1]))
    stack = []
    for num in numbers:
        if num == 0:
            if stack:
                stack.pop()
        else:
            stack.append(num)
    print(sum(stack))

if __name__ == "__main__":
    main()
