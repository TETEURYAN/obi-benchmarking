import sys

def main():
    input_data = sys.stdin.read().split()
    if input_data:
        n = int(input_data[0])
        print((n - 2) ** 3)
        print(6 * ((n - 2) ** 2))
        print(12 * (n - 2))
        print(8)

if __name__ == '__main__':
    main()