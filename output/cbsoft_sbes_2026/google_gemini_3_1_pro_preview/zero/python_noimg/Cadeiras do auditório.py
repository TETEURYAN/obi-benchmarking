import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    L = int(input_data[0])
    C = int(input_data[1])
    
    orig_R = []
    orig_C = []
    
    idx = 2
    for i in range(L):
        row_first = int(input_data[idx])
        orig_R.append((row_first - 1) // C)
        if i == 0:
            for j in range(C):
                val = int(input_data[idx + j])
                orig_C.append((val - 1) % C)
        idx += C
        
    swaps = []
    
    for i in range(L):
        while orig_R[i] != i:
            target = orig_R[i]
            swaps.append(('L', i + 1, target + 1))
            orig_R[i], orig_R[target] = orig_R[target], orig_R[i]
            
    for j in range(C):
        while orig_C[j] != j:
            target = orig_C[j]
            swaps.append(('C', j + 1, target + 1))
            orig_C[j], orig_C[target] = orig_C[target], orig_C[j]
            
    print(len(swaps))
    for swap in swaps:
        print(f"{swap[0]} {swap[1]} {swap[2]}")

if __name__ == '__main__':
    solve()