import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    a = [int(x) for x in input_data[1:n+1]]
    
    for i in range(1, n - 1):
        if a[i-1] > a[i] and a[i] < a[i+1]:
            print("S")
            return
            
    print("N")

if __name__ == '__main__':
    main()