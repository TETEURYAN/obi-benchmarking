import sys

def main():
    input_data = sys.stdin.read().split()
    if len(input_data) >= 2:
        p = int(input_data[0])
        r = int(input_data[1])
        if p == 0:
            print("C")
        elif r == 0:
            print("B")
        else:
            print("A")

if __name__ == '__main__':
    main()