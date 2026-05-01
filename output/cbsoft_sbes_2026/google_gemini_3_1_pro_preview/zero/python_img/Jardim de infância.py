
import sys

def solve():
    input_data = sys.stdin.read().split()
    if len(input_data) < 14:
        return
    
    pts = []
    for i in range(7):
        pts.append((int(input_data[2*i]), int(input_data[2*i+1])))
        
    P1, P2, P3, P4, P5, P6, P7 = pts
    
    def dist2(A, B):
        return (A[0] - B[0])**2 + (A[1] - B[1])**2
        
    def dot(A, B):
        return A[0]*B[0] + A[1]*B[1]
        
    def cross(A, B):
        return A[0]*B[1] - A[1]*B[0]
        
    def vec(A, B):
        return (B[0] - A[0], B[1] - A[1])
        
    v12 = vec(P1, P2)
    v13 = vec(P1, P3)
    if dot(v12, v13) <= 0:
        print("N")
        return
        
    if dist2(P1, P2) != dist2(P1, P3):
        print("N")
        return
        
    v23 = vec(P2, P3)
    v24 = vec(P2, P4)
    v25 = vec(P2, P5)
    if cross(v23, v24) != 0 or cross(v23, v25) != 0:
        print("N")
        return
        
    if P2[0] + P3[0] != P4[0] + P5[0] or P2[1] + P3[1] != P4[1] + P5[1]:
        print("N")
        return
        
    if dist2(P2, P3) <= dist2(P4, P5):
        print("N")
        return
        
    v46 = vec(P4, P6)
    v57 = vec(P5, P7)
    if dot(v46, v23) != 0 or dot(v57, v23) != 0:
        print("N")
        return
        
    if dist2(P4, P6) != dist2(P5, P7):
        print("N")
        return
        
    v21 = vec(P2, P1)
    v26 = vec(P2, P6)
    c1 = cross(v23, v21)
    c6 = cross(v23, v26)
    if c1 * c6 >= 0:
        print("N")
        return
        
    print("S")

if __name__ == '__main__':
    solve()
