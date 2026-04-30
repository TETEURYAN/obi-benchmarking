
def main():
    horizontal = input().strip()
    vertical = input().strip()

    max_h = -1
    max_v = -1
    found = False

    for i in range(len(horizontal)):
        for j in range(len(vertical)):
            if horizontal[i] == vertical[j]:
                if i > max_h or (i == max_h and j > max_v):
                    max_h = i
                    max_v = j
                    found = True

    if found:
        print(f"{max_h + 1} {max_v + 1}")
    else:
        print("-1 -1")

if __name__ == "__main__":
    main()
