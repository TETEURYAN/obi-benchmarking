
import sys

def main():
    data = sys.stdin.read().split()
    C = int(data[0])
    D = int(data[1])
    T = int(data[2])

    if T * C >= D:
        print("0.0")
        return

    remaining_distance = D - T * C
    fuel_needed = remaining_distance / C
    print("{0:.1f}".format(fuel_needed))

if __name__ == "__main__":
    main()
