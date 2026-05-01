import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    A = input_data[0]
    B = input_data[1]
    
    max_len = max(len(A), len(B))
    A = A.zfill(max_len)
    B = B.zfill(max_len)
    
    resA = []
    resB = []
    
    for i in range(max_len):
        da = int(A[i])
        db = int(B[i])
        
        if da > db:
            resA.append(A[i])
        elif da < db:
            resB.append(B[i])
        else:
            resA.append(A[i])
            resB.append(B[i])
            
    strA = "".join(resA)
    strB = "".join(resB)
    
    valA = int(strA) if strA else -1
    valB = int(strB) if strB else -1
    
    print(f"{min(valA, valB)} {max(valA, valB)}")

if __name__ == '__main__':
    solve()