import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    M = int(input_data[0])
    N = int(input_data[1])
    
    balance = [0] * (N + 1)
    orig_total = 0
    
    it = iter(input_data)
    next(it)
    next(it)
    
    for _ in range(M):
        X = int(next(it))
        V = int(next(it))
        Y = int(next(it))
        
        balance[X] -= V
        balance[Y] += V
        orig_total += V
        
    min_total = sum(b for b in balance if b > 0)
    
    if min_total < orig_total:
        print('S')
    else:
        print('N')
    print(min_total)

if __name__ == '__main__':
    main()