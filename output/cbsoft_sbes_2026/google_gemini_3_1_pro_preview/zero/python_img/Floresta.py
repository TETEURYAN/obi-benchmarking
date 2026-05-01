import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    N = int(input_data[0])
    
    M = 2 * N - 1
    ans = 0
    
    limit = int(M ** 0.5)
    for i in range(3, limit + 1, 2):
        if M % i == 0:
            ans += 1
            
    print(ans)

if __name__ == '__main__':
    main()