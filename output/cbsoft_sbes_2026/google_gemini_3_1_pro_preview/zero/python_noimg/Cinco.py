import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    D = [int(x) for x in input_data[1:N+1]]
    
    best_i = -1
    for i in range(N - 1):
        if D[i] == 0 or D[i] == 5:
            if D[i] < D[-1]:
                best_i = i
                break
            else:
                best_i = i
                
    if best_i == -1:
        print("-1")
    else:
        D[best_i], D[-1] = D[-1], D[best_i]
        print(" ".join(map(str, D)))

if __name__ == '__main__':
    solve()