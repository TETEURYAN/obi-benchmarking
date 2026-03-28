import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    sizes = list(map(int, data[1:1+n]))
    
    replace = 0
    repair = 0
    for s in sizes:
        if s < 50:
            replace += 1
        elif s < 85:
            repair += 1
    print(replace, repair)

if __name__ == "__main__":
    main()