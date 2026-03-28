import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    horizontal = data[0]
    vertical = data[1]

    best_h = -1
    best_v = -1
    for i in range(len(horizontal)):
        for j in range(len(vertical)):
            if horizontal[i] == vertical[j]:
                if best_h == -1:
                    best_h = i + 1
                    best_v = j + 1
                else:
                    if i + 1 > best_h:
                        best_h = i + 1
                        best_v = j + 1
                    elif i + 1 == best_h and j + 1 > best_v:
                        best_v = j + 1

    print(best_h, best_v)

if __name__ == "__main__":
    main()