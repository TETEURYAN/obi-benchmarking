
import sys

def main():
    placa = sys.stdin.readline().strip()
    if len(placa) == 8 and placa[3] == '-' and placa[:3].isalpha() and placa[4:].isdigit():
        print(1)
    elif len(placa) == 7 and placa[3].isdigit() and placa[4].isalpha() and placa[0:3].isalpha() and placa[5:].isdigit():
        print(2)
    else:
        print(0)

if __name__ == "__main__":
    main()
