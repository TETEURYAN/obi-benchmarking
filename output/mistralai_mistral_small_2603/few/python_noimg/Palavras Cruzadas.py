import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        print("-1 -1")
        return

    horizontal = data[0]
    vertical = data[1]

    max_h_index = -1
    max_v_index = -1

    for i in range(len(horizontal)):
        for j in range(len(vertical)):
            if horizontal[i] == vertical[j]:
                if i > max_h_index or (i == max_h_index and j > max_v_index):
                    max_h_index = i
                    max_v_index = j

    if max_h_index == -1:
        print("-1 -1")
    else:
        print(f"{max_h_index + 1} {max_v_index + 1}")

if __name__ == "__main__":
    main()