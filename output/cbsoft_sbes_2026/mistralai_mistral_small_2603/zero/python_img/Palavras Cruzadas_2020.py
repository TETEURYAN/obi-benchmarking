
def main():
    horizontal = input().strip()
    vertical = input().strip()

    best_i = -1
    best_j = -1

    for i in range(len(horizontal)):
        for j in range(len(vertical)):
            if horizontal[i] == vertical[j]:
                if best_i == -1 or i > best_i or (i == best_i and j > best_j):
                    best_i = i
                    best_j = j

    if best_i == -1:
        print("-1 -1")
    else:
        print(f"{best_i + 1} {best_j + 1}")

if __name__ == "__main__":
    main()
