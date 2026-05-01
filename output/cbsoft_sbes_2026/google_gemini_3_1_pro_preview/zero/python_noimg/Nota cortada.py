import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    B = int(input_data[0])
    T = int(input_data[1])
    
    if B + T > 160:
        print(1)
    elif B + T < 160:
        print(2)
    else:
        print(0)

if __name__ == '__main__':
    main()