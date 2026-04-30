import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    N = int(input_data[0])
    T = int(input_data[1])
    
    if T == 0:
        print(N)
    elif T == 1:
        print(N * (N - 1))
    elif T == 2:
        print(N * (N - 1) * (N - 2) // 6)

if __name__ == '__main__':
    main()