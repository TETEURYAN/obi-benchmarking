import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    x = int(input_data[0])
    y = int(input_data[1])
    
    if -8 <= x <= 8 and 0 <= y <= 8:
        print("S")
    else:
        print("N")

if __name__ == '__main__':
    main()