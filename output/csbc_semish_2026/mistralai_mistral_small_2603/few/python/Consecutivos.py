import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    values = list(map(int, data[1:n+1]))
    
    max_streak = 0
    current_streak = 0
    prev = None
    
    for num in values:
        if num == prev:
            current_streak += 1
        else:
            if current_streak > max_streak:
                max_streak = current_streak
            current_streak = 1
            prev = num
    
    if current_streak > max_streak:
        max_streak = current_streak
    
    print(max_streak)

if __name__ == "__main__":
    main()