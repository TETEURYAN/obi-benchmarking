import sys

def main():
    a = int(sys.stdin.readline().strip())
    m = int(sys.stdin.readline().strip())
    
    if a + m <= 50:
        print("S")
    else:
        print("N")

if __name__ == "__main__":
    main()