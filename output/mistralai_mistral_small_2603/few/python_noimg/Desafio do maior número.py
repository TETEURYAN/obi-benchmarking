import sys

def main():
    numbers = list(map(int, sys.stdin.read().split()))
    max_num = 0
    for num in numbers:
        if num == 0:
            break
        if num > max_num:
            max_num = num
    print(max_num)

if __name__ == "__main__":
    main()