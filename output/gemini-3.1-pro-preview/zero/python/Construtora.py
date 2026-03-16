
import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    a = [int(x) for x in input_data[1:n+1]]
    
    ans = max(a) - a[0]
    for i in range(n - 1):
        if a[i] > a[i+1]:
            ans += a[i] - a[i+1]
            
    print(ans)

if __name__ == '__main__':
    main()
