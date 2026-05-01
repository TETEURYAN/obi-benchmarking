
import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n1, n2, n3, n4 = map(int, input_data)
    
    if n1 == n3 or n2 == n4:
        print("V")
    else:
        print("F")

if __name__ == '__main__':
    main()
