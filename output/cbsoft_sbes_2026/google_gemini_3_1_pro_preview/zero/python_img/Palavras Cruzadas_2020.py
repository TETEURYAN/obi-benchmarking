import sys

def main():
    input_data = sys.stdin.read().split()
    if len(input_data) >= 2:
        h = input_data[0]
        v = input_data[1]
        
        for i in range(len(h) - 1, -1, -1):
            j = v.rfind(h[i])
            if j != -1:
                print(f"{i + 1} {j + 1}")
                return
        print("-1 -1")

if __name__ == '__main__':
    main()