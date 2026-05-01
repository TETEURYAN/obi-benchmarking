import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    T = int(input_data[1])
    
    top = input_data[2:N+2]
    bottom = input_data[N+2:2*N+2]
    
    flips = [0] * (N + 2)
    
    idx = 2 * N + 2
    for _ in range(T):
        I = int(input_data[idx])
        J = int(input_data[idx+1])
        flips[I] += 1
        flips[J+1] -= 1
        idx += 2
        
    current_flips = 0
    result = []
    for i in range(1, N + 1):
        current_flips += flips[i]
        if current_flips % 2 == 0:
            result.append(top[i-1])
        else:
            result.append(bottom[i-1])
            
    print(" ".join(result))

if __name__ == '__main__':
    main()