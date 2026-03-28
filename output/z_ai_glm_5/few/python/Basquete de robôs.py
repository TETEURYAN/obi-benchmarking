import sys

def main():
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    d = int(input_data[0])

    if d <= 800:
        print(1)
    elif d <= 1400:
        print(2)
    else:
        print(3)

if __name__ == "__main__":
    main()