import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    N = int(input_data[0])
    D = int(input_data[1])
    A = int(input_data[2])
    
    if D >= A:
        print(D - A)
    else:
        print(N - A + D)

if __name__ == '__main__':
    main()