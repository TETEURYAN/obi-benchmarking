
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0])
    x1 = int(data[1])
    x2 = int(data[2])
    lines = []
    index = 3
    for i in range(n):
        a = int(data[index])
        b = int(data[index + 1])
        index += 2
        lines.append((a, b))
    
    if x1 == x2:
        print(n * (n - 1) // 2)
        return
    
    events = []
    for a, b in lines:
        y1 = a * x1 + b
        y2 = a * x2 + b
        if y1 > y2:
            events.append((y1, 1))
            events.append((y2, -1))
        else:
            events.append((y2, 1))
            events.append((y1, -1))
    
    events.sort()
    
    active = 0
    intersections = 0
    for i in range(len(events)):
        y, typ = events[i]
        if typ == 1:
            active += 1
        else:
            active -= 1
        if i < len(events) - 1:
            next_y = events[i + 1][0]
            if next_y > y:
                intersections += active - 1
    
    print(intersections)

if __name__ == "__main__":
    main()
