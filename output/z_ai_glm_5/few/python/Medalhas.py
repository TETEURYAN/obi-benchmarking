import sys

def main():
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    t1 = int(input_data[0])
    t2 = int(input_data[1])
    t3 = int(input_data[2])

    swimmers = [(t1, 1), (t2, 2), (t3, 3)]
    swimmers.sort()

    print(swimmers[0][1])
    print(swimmers[1][1])
    print(swimmers[2][1])

if __name__ == "__main__":
    main()