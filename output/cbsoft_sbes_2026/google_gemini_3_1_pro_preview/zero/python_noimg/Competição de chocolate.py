import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    N = int(input_data[0])
    M = int(input_data[1])
    
    if N % (M + 1) == 0:
        print("Carlos")
    else:
        print("Paula")

if __name__ == '__main__':
    main()