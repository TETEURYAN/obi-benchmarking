
import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    trees = []
    idx = 1
    for _ in range(N):
        trees.append((int(input_data[idx]), int(input_data[idx+1])))
        idx += 2
        
    trees.sort(key=lambda t: t[0])
    
    stack = []
    for p3 in trees:
        while len(stack) >= 2:
            p1 = stack[-2]
            p2 = stack[-1]
            
            ax = p2[0] - p1[0]
            ay = p2[1] - p1[1]
            
            bx = p3[0] - p2[0]
            by = p3[1] - p2[1]
            
            if ax * by - ay * bx >= 0:
                stack.pop()
            else:
                break
        stack.append(p3)
        
    print(len(stack) - 1)

if __name__ == '__main__':
    solve()
