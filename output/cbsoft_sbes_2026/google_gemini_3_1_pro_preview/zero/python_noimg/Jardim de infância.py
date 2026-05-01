
import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    pts = []
    for i in range(7):
        pts.append((int(input_data[2*i]), int(input_data[2*i+1])))
        
    P1, P2, P3, P4, P5, P6, P7 = pts
    
    def dot(A, B, C, D):
        return (B[0]-A[0])*(D[0]-C[0]) + (B[1]-A[1])*(D[1]-C[1])
        
    def cross(A, B, C, D):
        return (B[0]-A[0])*(D[1]-C[1]) - (B[1]-A[1])*(D[0]-C[0])
        
    def dist2(A, B):
        return (B[0]-A[0])**2 + (B[1]-A[1])**2

    if dot(P1, P2, P1, P3) <= 0:
        print("N")
        return
    if cross(P1, P2, P1, P3) == 0:
        print("N")
        return
        
    if dist2(P1, P2) != dist2(P1, P3):
        print("N")
        return
        
    if cross(P2, P3, P2, P4) != 0 or cross(P2, P3, P2, P5) != 0:
        print("N")
        return
        
    if P2[0] + P3[0] != P4[0] + P5[0] or P2[1] + P3[1] != P4[1] + P5[1]:
        print("N")
        return
        
    if dist2(P2, P3) <= dist2(P4, P5):
        print("N")
        return
        
    if dot(P4, P6, P2, P3) != 0 or dot(P5, P7, P2, P3) != 0:
        print("N")
        return
        
    if dist2(P4, P6) != dist2(P5, P7):
        print("N")
        return
        
    c1 = cross(P2, P3, P2, P1)
    c2 = cross(P2, P3, P2, P6)
    if c1 * c2 >= 0:
        print("N")
        return
        
    print("S")

if __name__ == '__main__':
    solve()
