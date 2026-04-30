import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    ans = 0
    
    for i in range(n):
        c = int(input_data[1 + 2*i])
        s = int(input_data[2 + 2*i])
        diff = abs(c - s)
        ans += min(diff, 10 - diff)
        
    print(ans)

if __name__ == '__main__':
    main()