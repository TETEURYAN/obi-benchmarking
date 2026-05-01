import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    t = int(input_data[1])
    
    if t == 0:
        print(n)
    elif t == 1:
        print(n * (n - 1))
    elif t == 2:
        print(n * (n - 1) * (n - 2) // 6)

if __name__ == '__main__':
    main()