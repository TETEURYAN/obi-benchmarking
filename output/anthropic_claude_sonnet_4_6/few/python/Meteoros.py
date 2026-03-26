import sys

def main():
    data = sys.stdin.read().split()
    idx = 0
    test_num = 1
    
    while idx < len(data):
        X1 = int(data[idx]); Y1 = int(data[idx+1]); X2 = int(data[idx+2]); Y2 = int(data[idx+3])
        idx += 4
        
        if X1 == 0 and Y1 == 0 and X2 == 0 and Y2 == 0:
            break
        
        N = int(data[idx]); idx += 1
        
        count = 0
        for _ in range(N):
            X = int(data[idx]); Y = int(data[idx+1]); idx += 2
            if X1 <= X <= X2 and Y2 <= Y <= Y1:
                count += 1
        
        print(f"Teste {test_num}")
        print(count)
        print()
        test_num += 1

main()