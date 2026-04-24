import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    s = data[1]
    if n == 0:
        return
    compressed = []
    current_char = s[0]
    count = 1
    for i in range(1, n):
        if s[i] == current_char:
            count += 1
        else:
            compressed.append(f"{count} {current_char}")
            current_char = s[i]
            count = 1
    compressed.append(f"{count} {current_char}")
    print(' '.join(compressed))

if __name__ == "__main__":
    main()