import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    k = int(input_data[1])
    
    u = []
    for i in range(n):
        if input_data[2 + i] == '1':
            u.append(i)
            
    d = []
    for i in range(n):
        if input_data[2 + n + i] == '1':
            d.append(i)
            
    ans = sum(abs(u[i] - d[i]) for i in range(k))
    print(ans)

if __name__ == '__main__':
    main()