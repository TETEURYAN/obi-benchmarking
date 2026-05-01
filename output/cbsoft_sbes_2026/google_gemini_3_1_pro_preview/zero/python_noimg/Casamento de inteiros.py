import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    A = input_data[0]
    B = input_data[1]
    
    L = max(len(A), len(B))
    A = A.zfill(L)
    B = B.zfill(L)
    
    resA = []
    resB = []
    
    for i in range(L):
        if A[i] > B[i]:
            resA.append(A[i])
        elif A[i] < B[i]:
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
    main()