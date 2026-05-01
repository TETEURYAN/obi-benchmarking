import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    D = int(input_data[0])
    print((D - 5) % 8)

if __name__ == '__main__':
    main()