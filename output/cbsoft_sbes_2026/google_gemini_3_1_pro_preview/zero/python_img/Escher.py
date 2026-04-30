import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    a = [int(x) for x in input_data[1:n+1]]
    
    s = a[0] + a[-1]
    for i in range(n // 2 + 1):
        if a[i] + a[n - 1 - i] != s:
            print("N")
            return
    print("S")

if __name__ == '__main__':
    main()