import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    pos = []
    idx = 2
    for _ in range(n):
        p = m
        for j in range(m):
            if p == m and input_data[idx] != '0':
                p = j
            idx += 1
        pos.append(p)
        
    for i in range(n - 1):
        if pos[i] == m:
            if pos[i+1] != m:
                print('N')
                return
        else:
            if pos[i+1] <= pos[i]:
                print('N')
                return
                
    print('S')

if __name__ == '__main__':
    main()