import sys
import math

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    N = int(input_data[0])
    
    sums = [0] * N
    for i in range(1, len(input_data)):
        sums[(i - 1) % N] += int(input_data[i])
        
    fact = math.factorial(N - 1)
    expected_sum = fact * (N * (N + 1)) // 2
    
    ans = [str(expected_sum - s) for s in sums]
    print(" ".join(ans))

if __name__ == '__main__':
    main()