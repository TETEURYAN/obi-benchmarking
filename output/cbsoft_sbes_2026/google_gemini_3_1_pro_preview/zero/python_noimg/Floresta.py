import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    
    m = 2 * n - 1
    ans = 0
    
    a = 3
    while a * a <= m:
        if m % a == 0:
            ans += 1
        a += 2
        
    print(ans)

if __name__ == '__main__':
    main()