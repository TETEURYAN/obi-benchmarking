import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    L = int(input_data[0])
    C = int(input_data[1])
    
    if L < 2 or C < 2:
        print(0)
        return
        
    idx = 2
    prev_row = [int(x) for x in input_data[idx:idx+C]]
    idx += C
    
    max_area = 0
    heights = [0] * (C - 1)
    
    for _ in range(L - 1):
        curr_row = [int(x) for x in input_data[idx:idx+C]]
        idx += C
        
        for j in range(C - 1):
            if prev_row[j] + curr_row[j+1] <= prev_row[j+1] + curr_row[j]:
                heights[j] += 1
            else:
                heights[j] = 0
                
        stack = []
        for j in range(C - 1):
            h = heights[j]
            while stack and heights[stack[-1]] >= h:
                pos = stack.pop()
                height = heights[pos]
                if height > 0:
                    width = j if not stack else j - stack[-1] - 1
                    area = (height + 1) * (width + 1)
                    if area > max_area:
                        max_area = area
            stack.append(j)
            
        while stack:
            pos = stack.pop()
            height = heights[pos]
            if height > 0:
                width = (C - 1) if not stack else (C - 1) - stack[-1] - 1
                area = (height + 1) * (width + 1)
                if area > max_area:
                    max_area = area
                    
        prev_row = curr_row

    print(max_area)

if __name__ == '__main__':
    solve()