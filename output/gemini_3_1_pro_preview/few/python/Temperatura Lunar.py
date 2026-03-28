import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    idx = 0
    test_case = 1
    while idx < len(input_data):
        n = int(input_data[idx])
        m = int(input_data[idx+1])
        idx += 2
        
        if n == 0 and m == 0:
            break
            
        temps = [int(x) for x in input_data[idx:idx+n]]
        idx += n
        
        current_sum = sum(temps[:m])
        min_sum = current_sum
        max_sum = current_sum
        
        for i in range(m, n):
            current_sum += temps[i] - temps[i-m]
            if current_sum < min_sum:
                min_sum = current_sum
            if current_sum > max_sum:
                max_sum = current_sum
                
        min_avg = min_sum // m if min_sum >= 0 else -(-min_sum // m)
        max_avg = max_sum // m if max_sum >= 0 else -(-max_sum // m)
        
        print(f"Teste {test_case}")
        print(f"{min_avg} {max_avg}")
        print()
        
        test_case += 1

if __name__ == '__main__':
    solve()