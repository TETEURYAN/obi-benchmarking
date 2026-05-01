import sys

def main():
    input_data = sys.stdin.read().split()
    if len(input_data) >= 2:
        G = int(input_data[0])
        P = int(input_data[1])
        print(G * 8 + P * 4 - 2)

if __name__ == '__main__':
    main()