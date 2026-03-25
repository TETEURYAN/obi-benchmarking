import sys

def main():
    data = sys.stdin.read().strip()
    if not data:
        return
    D = int(data)
    bus_stops = [0, 400, 800, 1200, 1600, 2000]
    min_dist = float('inf')
    for stop in bus_stops:
        dist = abs(D - stop)
        if dist < min_dist:
            min_dist = dist
    print(min_dist)

if __name__ == "__main__":
    main()