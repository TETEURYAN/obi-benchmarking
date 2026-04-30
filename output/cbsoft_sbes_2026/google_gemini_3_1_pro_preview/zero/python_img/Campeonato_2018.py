import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    arr = list(map(int, input_data))
    
    pos1 = arr.index(1)
    pos9 = arr.index(9)
    
    if pos1 // 2 == pos9 // 2:
        print("oitavas")
    elif pos1 // 4 == pos9 // 4:
        print("quartas")
    elif pos1 // 8 == pos9 // 8:
        print("semifinal")
    else:
        print("final")

if __name__ == '__main__':
    main()