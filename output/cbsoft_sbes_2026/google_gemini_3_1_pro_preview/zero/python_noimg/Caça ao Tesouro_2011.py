import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    K = int(input_data[1])
    
    clues = []
    idx = 2
    for _ in range(K):
        clues.append((int(input_data[idx]), int(input_data[idx+1]), int(input_data[idx+2])))
        idx += 3
        
    ans_x, ans_y = -1, -1
    count = 0
    
    for x in range(N):
        for y in range(N):
            possible = True
            for cx, cy, cd in clues:
                if abs(x - cx) + abs(y - cy) != cd:
                    possible = False
                    break
            if possible:
                ans_x, ans_y = x, y
                count += 1
                if count > 1:
                    print("-1 -1")
                    return
                    
    if count == 1:
        print(f"{ans_x} {ans_y}")
    else:
        print("-1 -1")

if __name__ == '__main__':
    main()