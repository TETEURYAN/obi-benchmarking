
import sys

input = sys.stdin.read
data = input().split()

index = 0
test = 1

while True:
    N = int(data[index])
    index += 1
    if N == 0:
        break
    
    # Initialize intersection with first rectangle
    if N == 0:
        inter_x1 = -10001
        inter_y1 = -10001
        inter_x2 = 10001
        inter_y2 = 10001
    else:
        x1 = int(data[index])
        y1 = int(data[index+1])
        x2 = int(data[index+2])
        y2 = int(data[index+3])
        index += 4
        inter_x1 = min(x1, x2)
        inter_y1 = max(y1, y2)
        inter_x2 = max(x1, x2)
        inter_y2 = min(y1, y2)
    
    for i in range(1, N):
        x1 = int(data[index])
        y1 = int(data[index+1])
        x2 = int(data[index+2])
        y2 = int(data[index+3])
        index += 4
        r_left = min(x1, x2)
        r_top = max(y1, y2)
        r_right = max(x1, x2)
        r_bottom = min(y1, y2)
        
        inter_x1 = max(inter_x1, r_left)
        inter_y1 = min(inter_y1, r_top)
        inter_x2 = min(inter_x2, r_right)
        inter_y2 = max(inter_y2, r_bottom)
    
    print(f"Teste {test}")
    if inter_x1 < inter_x2 and inter_y2 < inter_y1:
        print(inter_x1, inter_y1, inter_x2, inter_y2)
    else:
        print("nenhum")
    print()
    test += 1
