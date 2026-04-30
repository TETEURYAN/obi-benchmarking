import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    A = int(input_data[0])
    M = int(input_data[1])
    
    if A + M <= 50:
        print("S")
    else:
        print("N")

if __name__ == '__main__':
    main()