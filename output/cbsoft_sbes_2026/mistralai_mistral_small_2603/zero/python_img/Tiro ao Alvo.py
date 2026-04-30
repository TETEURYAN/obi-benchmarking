
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    C = int(data[0])
    T = int(data[1])
    radii = list(map(int, data[2:2+C]))
    shots = []
    index = 2 + C
    for i in range(T):
        x = int(data[index])
        y = int(data[index+1])
        index += 2
        shots.append((x, y))
    
    total_points = 0
    for (x, y) in shots:
        distance_sq = x*x + y*y
        points = 0
        for r in radii:
            if distance_sq <= r*r:
                points += 1
            else:
                break
        total_points += points
    
    print(total_points)

if __name__ == "__main__":
    main()
