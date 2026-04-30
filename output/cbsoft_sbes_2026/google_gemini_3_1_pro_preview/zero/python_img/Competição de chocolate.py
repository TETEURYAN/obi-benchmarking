
import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    m = int(input_data[1])
    
    if n % (m + 1) == 0:
        print("Carlos")
    else:
        print("Paula")

if __name__ == '__main__':
    main()
