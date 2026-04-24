import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    grid = data[1:1+n]

    max_food = 0
    current_food = 0

    for i in range(n):
        if i % 2 == 0:
            row = grid[i]
            for j in range(n):
                cell = row[j]
                if cell == 'o':
                    current_food += 1
                elif cell == 'A':
                    if current_food > max_food:
                        max_food = current_food
                    current_food = 0
            if current_food > max_food:
                max_food = current_food
        else:
            row = grid[i]
            for j in range(n-1, -1, -1):
                cell = row[j]
                if cell == 'o':
                    current_food += 1
                elif cell == 'A':
                    if current_food > max_food:
                        max_food = current_food
                    current_food = 0
            if current_food > max_food:
                max_food = current_food

    print(max_food)

if __name__ == "__main__":
    main()