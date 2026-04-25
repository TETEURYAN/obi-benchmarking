import sys

def main():
    data = sys.stdin.read().split()
    Cv, Ce, Cs, Fv, Fe, Fs = map(int, data)
    
    C_points = Cv * 3 + Ce
    F_points = Fv * 3 + Fe
    
    if C_points > F_points:
        print('C')
    elif F_points > C_points:
        print('F')
    else:
        if Cs > Fs:
            print('C')
        elif Fs > Cs:
            print('F')
        else:
            print('=')

if __name__ == "__main__":
    main()