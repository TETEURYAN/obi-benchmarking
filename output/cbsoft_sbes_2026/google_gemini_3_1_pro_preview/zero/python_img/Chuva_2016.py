
import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    h = [int(x) for x in input_data[1:]]
    
    actual_n = len(h)
    if actual_n == 0:
        print(0)
        return
        
    left_max = [0] * actual_n
    right_max = [0] * actual_n
    
    left_max[0] = h[0]
    for i in range(1, actual_n):
        left_max[i] = left_max[i-1] if left_max[i-1] > h[i] else h[i]
        
    right_max[actual_n-1] = h[actual_n-1]
    for i in range(actual_n-2, -1, -1):
        right_max[i] = right_max[i+1] if right_max[i+1] > h[i] else h[i]
        
    ans = 0
    for i in range(actual_n):
        m = left_max[i] if left_max[i] < right_max[i] else right_max[i]
        if m > h[i]:
            ans += 1
            
    print(ans)

if __name__ == '__main__':
    main()
