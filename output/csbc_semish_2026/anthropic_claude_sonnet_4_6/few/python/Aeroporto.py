import sys

def main():
    data = sys.stdin.read().split()
    idx = 0
    test_num = 1
    
    while idx < len(data):
        A = int(data[idx]); V = int(data[idx+1])
        idx += 2
        
        if A == 0 and V == 0:
            break
        
        count = [0] * (A + 1)
        
        for _ in range(V):
            x = int(data[idx]); y = int(data[idx+1])
            idx += 2
            count[x] += 1
            count[y] += 1
        
        max_val = max(count[1:A+1])
        winners = [i for i in range(1, A+1) if count[i] == max_val]
        
        print(f"Teste {test_num}")
        print(*winners)
        print()
        
        test_num += 1

main()