import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    H, P, F, D = map(int, data)
    if D == 1:
        dist_FH = (H - F) % 16
        dist_FP = (P - F) % 16
    else:
        dist_FH = (F - H) % 16
        dist_FP = (F - P) % 16
    print("N" if dist_FP < dist_FH else "S")

if __name__ == "__main__":
    main()