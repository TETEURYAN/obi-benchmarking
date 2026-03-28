import sys

def main():
    directions = ['norte', 'leste', 'sul', 'oeste']
    pos = {d: i for i, d in enumerate(directions)}
    a, b = sys.stdin.read().split()
    dir_a = pos[a]
    dir_b = pos[b]
    diff = abs(dir_a - dir_b)
    angle = min(diff * 90, (4 - diff) * 90)
    print(angle)

if __name__ == "__main__":
    main()