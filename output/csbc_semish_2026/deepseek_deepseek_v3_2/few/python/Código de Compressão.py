import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    s = data[1] if len(data) > 1 else ""
    
    result = []
    i = 0
    while i < n:
        count = 1
        while i + count < n and s[i + count] == s[i]:
            count += 1
        result.append(f"{count} {s[i]}")
        i += count
    
    print(" ".join(result))

if __name__ == "__main__":
    main()