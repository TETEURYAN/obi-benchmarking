import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    it = iter(input_data)
    next(it)
    
    trees = [(int(x), int(y)) for x, y in zip(it, it)]
    trees.sort(key=lambda item: item[0])
    
    stack = []
    for p in trees:
        px, py = p
        while len(stack) >= 2:
            Ax, Ay = stack[-2]
            Bx, By = stack[-1]
            
            cp = (Bx - Ax) * (py - By) - (By - Ay) * (px - Bx)
            
            if cp >= 0:
                stack.pop()
            else:
                break
        stack.append(p)
        
    print(len(stack) - 1)

if __name__ == '__main__':
    solve()