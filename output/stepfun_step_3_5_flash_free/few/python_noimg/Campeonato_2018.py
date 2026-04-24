import sys

def main():
    data = sys.stdin.read().split()
    nums = list(map(int, data))
    pos1 = pos9 = None
    for i, x in enumerate(nums, start=1):
        if x == 1:
            pos1 = i
        elif x == 9:
            pos9 = i
    if (pos1 - 1) // 2 == (pos9 - 1) // 2:
        print("oitavas")
    elif (pos1 - 1) // 4 == (pos9 - 1) // 4:
        print("quartas")
    elif (pos1 - 1) // 8 == (pos9 - 1) // 8:
        print("semifinal")
    else:
        print("final")

if __name__ == "__main__":
    main()