import sys

def main():
    input_data = sys.stdin.read().split()
    if len(input_data) >= 3:
        A = int(input_data[0])
        B = int(input_data[1])
        C = int(input_data[2])
        
        if B - A < C - B:
            print(1)
        elif B - A > C - B:
            print(-1)
        else:
            print(0)

if __name__ == '__main__':
    main()