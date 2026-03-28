import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

pts = []
for i in range(7):
    pts.append((int(input_data[2*i]), int(input_data[2*i+1])))
    
x1, y1 = pts[0]
x2, y2 = pts[1]
x3, y3 = pts[2]
x4, y4 = pts[3]
x5, y5 = pts[4]
x6, y6 = pts[5]
x7, y7 = pts[6]

v12x, v12y = x2 - x1, y2 - y1
v13x, v13y = x3 - x1, y3 - y1
if v12x * v13x + v12y * v13y <= 0:
    print("N")
    exit()
    
if v12x**2 + v12y**2 != v13x**2 + v13y**2:
    print("N")
    exit()
    
v23x, v23y = x3 - x2, y3 - y2
v24x, v24y = x4 - x2, y4 - y2
v25x, v25y = x5 - x2, y5 - y2
if v23x * v24y - v23y * v24x != 0:
    print("N")
    exit()
if v23x * v25y - v23y * v25x != 0:
    print("N")
    exit()
    
if x2 + x3 != x4 + x5 or y2 + y3 != y4 + y5:
    print("N")
    exit()
    
v45x, v45y = x5 - x4, y5 - y4
if v23x**2 + v23y**2 <= v45x**2 + v45y**2:
    print("N")
    exit()
    
v46x, v46y = x6 - x4, y6 - y4
v57x, v57y = x7 - x5, y7 - y5
if v46x * v23x + v46y * v23y != 0:
    print("N")
    exit()
if v57x * v23x + v57y * v23y != 0:
    print("N")
    exit()
    
if v46x**2 + v46y**2 != v57x**2 + v57y**2:
    print("N")
    exit()
    
v21x, v21y = x1 - x2, y1 - y2
v26x, v26y = x6 - x2, y6 - y2
cross1 = v23x * v21y - v23y * v21x
cross6 = v23x * v26y - v23y * v26x
if cross1 * cross6 >= 0:
    print("N")
    exit()
    
print("S")