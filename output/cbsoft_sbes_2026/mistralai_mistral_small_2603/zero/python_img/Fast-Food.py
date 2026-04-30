
import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    X = list(map(int, data[1:n+1]))
    Y = list(map(int, data[n+1:2*n+1]))

    points = list(zip(X, Y))

    def distance(p1, p2):
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

    def min_max_distance(points):
        points_sorted_x = sorted(points, key=lambda p: (p[0], p[1]))
        points_sorted_y = sorted(points, key=lambda p: (p[1], p[0]))

        def get_min_max(partition):
            if not partition:
                return 0
            max_dist = 0
            for i in range(len(partition)):
                for j in range(i+1, len(partition)):
                    dist = distance(partition[i], partition[j])
                    if dist > max_dist:
                        max_dist = dist
            return max_dist

        def backtrack(index, set1, set2):
            if index == n:
                d1 = get_min_max(set1)
                d2 = get_min_max(set2)
                return max(d1, d2)
            if len(set1) > n//2 or len(set2) > n//2:
                return float('inf')
            res = float('inf')
            set1.append(points[index])
            res = min(res, backtrack(index + 1, set1, set2))
            set1.pop()
            set2.append(points[index])
            res = min(res, backtrack(index + 1, set1, set2))
            set2.pop()
            return res

        return backtrack(0, [], [])

    print(min_max_distance(points))

if __name__ == "__main__":
    main()
