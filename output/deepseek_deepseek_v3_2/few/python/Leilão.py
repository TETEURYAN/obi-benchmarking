import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    idx = 0
    n = int(data[idx])
    idx += 1
    best_name = ""
    best_val = -1
    for _ in range(n):
        name = data[idx]
        idx += 1
        val = int(data[idx])
        idx += 1
        if val > best_val:
            best_val = val
            best_name = name
    sys.stdout.write(f"{best_name}\n{best_val}\n")

if __name__ == "__main__":
    main()